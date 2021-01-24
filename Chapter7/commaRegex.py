import re

def findMatch(number):
    commaRegex = re.compile(r'(^\d{1,3})(,\d{3})*$')

    match = commaRegex.search(number)
    
    if match == None:
        print('No Match')
    else:
        print('Match:' + match.group())

Numbers = ['42', '1,234', '6,368,745', '12,34,567', '1234']

for i in Numbers:
    findMatch(i)