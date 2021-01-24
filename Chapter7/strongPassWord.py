#! python3
# strongPassWord.py - checks for strong passwords

import re

def checkPassword(password):
    
    #isStrong = False
    reason = ''
    
    checkLength = re.compile(r'\w{8,}') # Check if the password is at least eight characters
    checkUpper = re.compile(r'[A-Z]+') # Check if the password contains uppercase letters
    checkLower = re.compile(r'[A-Z]+') # Check if the password contains lowercase letters
    checkDigits = re.compile(r'\d+') # Check if the password contains at least one digit
    
    if checkLength.search(password) is None:
        reason = 'Password must be at least 8 characters long'
        return False, reason
    elif checkUpper.search(password) is None:
        reason = 'Password must contain both uppercase and lowercase letters'
        return False, reason
    elif checkLower.search(password) is None:
        reason = 'Password must contain both uppercase and lowercase letters'
        return False, reason
    elif checkDigits.search(password) is None:
        reason = 'Password must contain at lease one digit'
        return False, reason
    else:
        return True, reason
    
providedPassword = input('Please provide a password to check: ')
passwordStrong, reason = checkPassword(providedPassword)

if passwordStrong:
    print('Password is strong')
else:
    print('Password is not strong enough:')
    print('\t' + reason)