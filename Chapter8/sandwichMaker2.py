import pyinputplus as pyip


BREAD_PRICE = {'white': 2.00, 'wheat': 2.50, 'sour dough': 3.00}
PROTEIN_PRICE = {'chicken': 2.50, 'turkey': 2.25, 'ham': 1.75, 'tofu': 4.00}
CHEESE_PRICE = {'cheddar': 1.00, 'swiss': 1.25, 'mozzarella': 2.00}
EXTRA_PRICE = {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.30, 'tomato': 0.50}

# Function that gets the customer's order.
def customer_order(category, options):
    prompt = 'Please choose your ' + category + ': \n'
    choices = list(options.keys())
    choice = pyip.inputMenu(choices, prompt, lettered=True)
    return choice

def order_cheese(category, options):
    prompt = 'Would you like ' + category + '?\n'
    wants_cheese = pyip.inputYesNo(prompt)
    if wants_cheese == 'yes':
        choice = customer_order(category, options)
        return choice
    else:
        return None
    
def order_extras(options):
    extras = []
    for option in options.keys():
        prompt = 'Would you like ' + option + '?\n'
        wants_option = pyip.inputYesNo(prompt)
        if wants_option ==  'yes':
            extras.append(option)
    return extras

def sandwich_price(bread, protein, cheese, extras):
    price = BREAD_PRICE[bread] + PROTEIN_PRICE[protein]
    if cheese:
        price += CHEESE_PRICE[cheese]
    if extras:
        for extra in extras:
            price += EXTRA_PRICE[extra]
    return price

def number_of_sandwiches():
    prompt = 'How many sandwiches would you like?\n'
    minimum = 1
    number = pyip.inputInt(prompt, min=minimum)
    return number

# Test the price calculator
# assert sandwich_price('white', 'turkey', 'cheddar', ['lettuce']) == 5.55
# assert sandwich_price('sour dough', 'tofu', 'swiss',
#                       ['mayo', 'mustard', 'lettuce', 'tomato']) == 9.55

def main():
    bread_order = customer_order('bread', BREAD_PRICE)
    protein_order = customer_order('protein', PROTEIN_PRICE)
    cheese_order = order_cheese('cheese', CHEESE_PRICE)
    extras_order = order_extras(EXTRA_PRICE)
    sandwich_quantity = number_of_sandwiches()
    sandwich_total = sandwich_price(bread_order, protein_order, cheese_order,
                                extras_order)
    order_total = '{:.2f}'.format(sandwich_total * sandwich_quantity)
    
    print('Your order total is:\n' + '$' + str(order_total))

if __name__ == '__main__':
    main()