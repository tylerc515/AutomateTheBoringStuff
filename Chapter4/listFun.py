import random

spam = ['cat', 'bat', 'rat', 'elephant', 'lion', 'giraffe', 'zebra']

firstAnimal = random.randint(0,6)
secondAnimal = random.randint(0,6)

print('The ' + spam[firstAnimal] + ' ate the ' + spam[secondAnimal] + '.')