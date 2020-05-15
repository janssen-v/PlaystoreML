import csv

array = []


with open('train.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    
    # Assign data to list
    for row in my_reader:
        array.append(row)

    train_data = array[1:]
    # print(type(train_data[0][0]))
    pholder = []
    float_list = []
    for a in train_data:
        for b in a:
            pholder.append(float(b))
        float_list.append(pholder)

training_data = float_list

header = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']

def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)



class Question:


    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))


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

def info_gain(left, right, current_uncertainty):

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


class Decision_Node:


    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
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


    return Decision_Node(question, true_branch, false_branch)

def classify(row, node):


    if isinstance(node, Leaf):
        return node.predictions
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def print_leaf(counts):
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

if __name__ == '__main__':

    my_tree = build_tree(training_data)

    array2 = []
    with open('train.csv', 'r') as file:
        my_reader = csv.reader(file, delimiter=',')
        
        # Assign data to list
        for row in my_reader:
            array2.append(row)

        test_data = array[1:]

        pholder2 = []
        float_list2 = []
        for a in test_data:
            for b in a:
                pholder2.append(float(b))
            float_list2.append(pholder2)

    testing_data = float_list2

    n = 0
    j = 0

    # for row in testing_data:
    #     print(list(classify(row,my_tree)))
    
    for row in testing_data:
        k = (list(classify(row,my_tree))[0] > 6)
        m = ((row[-1]) > 6)
        if k == m:
            n+=1
            j+=1
        else:
            n+=1
    
    accuracy = (j/n)*100
    print('{0:1.4f}%'.format(accuracy))
