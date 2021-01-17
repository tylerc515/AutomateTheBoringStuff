def commaCode(userList):
    commaSeparated = ''
    if len(userList) == 0:
        print('Your list is empty')
    else:
        for i in range(len(userList)):
            if i < len(userList) - 1:
                commaSeparated += userList[i] + ', '
            elif i == len(userList) - 1:
                commaSeparated += 'and ' + userList[i]
        print(commaSeparated)

#myList = ['Gorilla', 'Elephant', 'Giraffe', 'Lion']
myList = []
commaCode(myList)

