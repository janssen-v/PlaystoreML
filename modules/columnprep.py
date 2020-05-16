# Prepare row for tree split
from modules.labelize import labelize

def columnprep(array, selected_column):
    # Array format -> list in list, rows and columns, returns the selected column labelized
    tempColumn = []
    for row in range(len(array)):
        tempColumn.append(row[selected_column])
    return labelize(tempColumn)
