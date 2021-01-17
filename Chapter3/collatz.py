def collatz(number):
    if number % 2 == 0:
        number /= 2
        print(str(int(number)))
        return number
    else:
        number = 3 * number + 1
        print(str(int(number)))
        return number

# asks for a number and runs colltz function until it returns 1
print('Please type in a number')
while True:
    try:
        typedNumber = int(input())
        break
    except ValueError:
            print('You did not enter an integer. Please enter an integer.')

newNumber = collatz(typedNumber)

while not newNumber == 1:
    newNumber = collatz(newNumber)
