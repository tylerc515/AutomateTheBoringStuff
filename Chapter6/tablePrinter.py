#! python3

def printTable(tableData):
    colWidths = [0] * len(tableData)


    for items in tableData:
        for item in items:
            if len(item) > colWidths[tableData.index(items)]:
                colWidths[tableData.index(items)] = len(item)

    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
                print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)