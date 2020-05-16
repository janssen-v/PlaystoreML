# Prepare row for tree split

def labelize(categories):
    uniqueCategories = []
    newCategories = []
    for i in range(len(categories)):
        if categories[i] not in uniqueCategories:
            uniqueCategories.append(categories[i])

    numeratedCategories = list(enumerate(uniqueCategories))

    for i in range(len(categories)):
        for j in range(len(numeratedCategories)):
            if numeratedCategories[j][1] == categories[i]:
                newCategories.append(numeratedCategories[j][0])
    
    return newCategories

def columnPrep(array, selected_column):
    # Array format -> list in list, rows and columns, returns the selected column labelized
    tempColumn = []
    for row in range(len(array)):
        tempColumn.append(array[row][selected_column-1])
    tempColumn = labelize(tempColumn)
    for row in range(len(array)):
        array[row][selected_column-1] = tempColumn.pop(0)
    return array

if __name__ == "__main__":
    array = [['dog', 'cat', 'mouse'],['bear', 'snake', 'rabbit'], ['ant', 'iguana', 'meerkat']]
    test = columnPrep(array, 1)
    print(test)