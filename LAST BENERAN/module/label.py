# Enumerates categories into labels

def labelize(categories):
    uniqueCategories = []
    newCategories = []
    for i in len(range(categories)):
        if categories[i] not in uniqueCategories:
            uniqueCategories.append(categories[i])

    numeratedCategories = list(enumerate(uniqueCategories))

    for i in len(range(categories)):
        for j in len(range(numeratedCategories)):
            if numeratedCategories[j][1] == categories[i]:
                newCategories.append(numeratedCategories[j][0])
    
    return newCategories
