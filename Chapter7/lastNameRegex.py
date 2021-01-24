import re

def findMatch(name):
    lastNameRegex = re.compile(r'([A-Z]{1}[A-Za-z]+) (Watanabe)$')

    match = lastNameRegex.search(name)
    
    if match == None:
        print(name + ' **does not match**')
    else:
        print(name + ' matches')

names = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']

for i in names:
    findMatch(i)