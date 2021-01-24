import re

def findMatch(words):
    lastNameRegex = re.compile(r'(alice|bob|carol) (eats|pets|throws) (apples|cats|baseballs)(.)?', re.I)

    match = lastNameRegex.search(words)
    
    if match == None:
        print(words + ' **does not match**')
    else:
        print(words + ' matches')

words = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws apples.', 
         'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS', 'Carol eats 7 cats']

for i in words:
    findMatch(i)