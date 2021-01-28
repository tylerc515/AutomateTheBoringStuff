import pyinputplus as pyip

# store a dictionary of ingredients and their respective prices
optionPrices = {'white' : 2.00,
                'wheat' : 2.50,
                'sour dough' : 3.00,
                'chicken' : 2.50,
                'turkey' : 2.25,
                'ham' : 1.75,
                'tofu' : 4.00,
                'cheddar' : 1.00,
                'swiss' : 1.25,
                'mozzarella' : 2.00,
                'mayo' : 0.25,
                'mustard' : 0.25,
                'lettuce' : 0.30,
                'tomato' : 0.50
                }

customerOrder = [] # a list to store the current order
extras = ['mayo', 'mustard', 'lettuce', 'tomato']
sandwichTotal = 0.0

# ask the user for bread choice and append to order list
breadChoice = pyip.inputMenu(['white', 'wheat', 'sour dough'], 
                             'Please choose your bread:\n', lettered=True)
customerOrder.append(breadChoice)

# ask the user for protein choice and append to order list
proteinChoice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 
                               'Please choose your protein:\n', lettered=True)
customerOrder.append(proteinChoice)

# ask if the user wants cheese, and if so, record cheese choice
cheeseResponse = pyip.inputYesNo('Would you like cheese?\n')
if cheeseResponse == 'yes':
    cheeseChoice = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], 
                                  'Please choose your cheese:\n', 
                                  lettered=True)
    customerOrder.append(cheeseChoice)
else:
    cheeseChoice = ''

# loop through 'extras' and ask if customer wants each one.
# If so, append it the order
choice = ''
for i in extras:
    choice = pyip.inputYesNo('Would you like ' + i +'?\n')
    if choice == 'yes':
        customerOrder.append(i)
    else:
        choice = ''

# get the number of sandwiches from the customer
numSandwiches = pyip.inputInt('How many sandwiches would you like?\n', min=1)

print('\nYour order: ')
# check if the item exists in the options, and get the price for each sandwich
for item in customerOrder:
    if item in optionPrices.keys():
        sandwichTotal += optionPrices.get(item)
        print('\t' + item + ' - $' + str(optionPrices.get(item)))

# per sandwhich total
print('Total for your sandwich: $' + str('{:0.2f}'.format(sandwichTotal))) 

print('Total for your order: (' + str(numSandwiches) + ' sandwiches @ $' + 
      str('{:0.2f}'.format(sandwichTotal)) + ' each): ')

# give the total price of sandwiches
print('$' + str('{:0.2f}'.format(sandwichTotal * numSandwiches)))

