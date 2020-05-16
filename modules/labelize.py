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

if __name__ == "__main__":
    cat = ['A','B','C','A','B','C','A','G','C','G','B','C','G','F','C','A','E','D']
    n_cat = labelize(cat)
    print(n_cat)