"""Calculator Program"""

print("Enter an operation to perform ")
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

operation = input()
while operation not in ['1','2','3','4']:
    print('Invalid input, try again')    
    operation = input()

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if operation == '1':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = add(num1, num2)
    print(f'{num1} + {num2} = {result}') 
elif operation == '2':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = subtract(num1, num2)
    print(f'{num1} - {num2} = {result}') 
elif operation == '3':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = multiply(num1, num2)
    print(f'{num1} * {num2} = {result}') 
elif operation == '4':
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    while num2 == 0:
        print('Cannot divide by zero, enter another number')
        num2 = int(input('Enter second number: '))
    result = divide(num1, num2)
    print(f'{num1} / {num2} = {result}') 