#! python3
# A date detection regex and validator

import re

def detectDate(date):
# Capture the date with regex in DD/MM/YYYY format
    dateDetection = re.compile(r'''
                            ([0-3][0-9])    # Capture the day
                            /               # / separator          
                            ([0-1][0-2])    # capture the month
                            /               # / separator
                            ([1-2][0-9]{3})   # capture the year
                            ''', re.VERBOSE)
    
    detectedDate = dateDetection.search(date)
    
    return detectedDate
 
# validate the date
def validateDate(detectedDate):
    day = detectedDate.group(1)
    month = detectedDate.group(2)
    year = detectedDate.group(3)
    months30 = ['04', '06', '09', '11'] # months with 30 days
    leapYear = False
    dateIsValid = False
    
    
    if month != '00' and day != '00':   # month and day are not '00'
        # check if the year is a leap year
        if int(year) % 4 == 0:
            if int(year) % 100 == 0:
                if int(year) % 400 == 0:
                    leapYear = True
            else:
                leapYear = True
                
        # if it is a leap year, ensure February can handle 29 days. If not, only allow 28
        if leapYear:
            if month == '02':
                if int(day) > 29:
                    dateIsValid = False
                else:
                    dateIsValid = True
        else:
            if month == '02':
                if int(day) > 28:
                    dateIsValid = False
                else:
                    dateIsValid = True
                    
            # If the month is April, June, September, or November, make sure it has maximum of 30 days
            elif month in months30:
                if int(day) > 30:
                    dateIsValid = False
                else:
                    dateIsValid = True
            else:   # date is not february 
                if int(day) > 31:
                    dateIsValid = False
                else:
                    dateIsValid = True
    else:
        dateIsValid = False
    
    if dateIsValid:
        print('%s/%s/%s is a valid date' % (day, month, year))
    else:
        print('****%s/%s/%s is a NOT valid date' % (day, month, year))

detectedDate = detectDate('29/02/2004')

if detectedDate != None:
    validateDate(detectedDate)
else:
    print('Date is not in valid format. Please enter date in DD/MM/YYYY format.')