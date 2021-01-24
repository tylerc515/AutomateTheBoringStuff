#! python3
# stripRegex.py - Regex version of the strip() method

import re

def stripRegex(userInput, replaceCharacter=''):
    
    replaceLeadingRegex = re.compile(r'^\s+') # replace leading whitespace
    replaceTrailingRegex = re.compile(r'\s+$') # replace trailing whitespace
    replaceCharRegex = re.compile(replaceCharacter) # replace the character specified by the user
    replacedInput = ''
    
    if replaceCharacter == '': # if the user did not supply a replacement character or specified ''
        replacedInput = replaceLeadingRegex.sub('', userInput)
        replacedInput = replaceTrailingRegex.sub('', replacedInput)
    else: # user did specify character to replace - replace user specified character with ''
        replacedInput = replaceCharRegex.sub('', userInput) 
        
    return replacedInput

replacedString = stripRegex('My name is Tyler', '5')
print('New string: ' + replacedString)