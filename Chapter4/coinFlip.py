import random

numberOfStreaks = 0
streak = 0

for experimentNumber in range(10000):
    result = []
    counter = 0
    for flip in range(100):
        result.append(random.randint(0,1))

    for i in result:
        if result[i] == result[i - 1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            numberOfStreaks += 1

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))