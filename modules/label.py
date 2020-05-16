# Enumerates categories into labels

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