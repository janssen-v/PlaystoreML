import csv
import os                   # For getting script directory (multi-device support)
from pathlib import Path    # Used for easy path referencing

this_folder = os.path.dirname(os.path.abspath(__file__))
p = Path(this_folder)
path = str(p.parent) + '/train.csv'

array = []
with open(path, 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    
    for row in my_reader:   # Allocates data from csv into a list
        array.append(row)

    train_data = array[1:]
    pholder = []
    float_list = []
    for a in train_data:
        pholder = []
        for b in a:
            pholder.append(float(b))
        float_list.append(pholder)

training_data = float_list

def unique_vals(rows, col): # Finds unique values for a column in a dataset
    return set([row[col] for row in rows])

def class_counts(rows): # Counts the number of each type of sample in a dataset
    counts = {}         # a dictionary of label -> count
    for row in rows:    # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value): # Test if a value is numeric
    return isinstance(value, int) or isinstance(value, float)

class Question:
    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, sample): # Compares the feature value in a sample to the feature value in this section
        val = sample[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

def partition(rows, question):
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty): # Gets information gain
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def find_best_split(rows):
    best_gain = 0
    best_question = None  
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  

    for col in range(n_features): 
        values = set([row[col] for row in rows])  
        for val in values: 
            question = Question(col, val)
            true_rows, false_rows = partition(rows, question)
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)
            
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

class Leaf:
    def __init__(self, rows):
        self.predictions = class_counts(rows)

class Node:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(rows):
    gain, question = find_best_split(rows)
    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)
    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)
    return Node(question, true_branch, false_branch)

def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

if __name__ == '__main__':
    my_tree = build_tree(training_data)
    path2 = str(p.parent) + '/test.csv' # References the current location of the test data
    array2 = []

    with open(path2, 'r') as file:
        my_reader2 = csv.reader(file, delimiter=',')
        for row in my_reader2:   # Assign data to list
            array2.append(row)
        test_data = array2[1:]
        pholder2 = []
        float_list2 = []
        for a in test_data:
            pholder2 = []
            for b in a:
                b = float(b)
                pholder2.append(b)
            float_list2.append(pholder2)
    
    testing_data = float_list2
    n = 0
    j = 0

    for row in testing_data:
        k = list(classify(row,my_tree))[0] > 6
        m = row[-1] > 6
        if k == m:
            j+=1
        n += 1
    accuracy = float(j)/float(n)*100
    print('Accuracy > ', end='')
    print('{0:1.4f}%'.format(accuracy))
