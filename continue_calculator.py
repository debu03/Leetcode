
while True:
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    op = input('Choose operation to be performed: ')

    if op == '+':
        print('Addition of numbers are:', num1 + num2)

    elif op == '-':
        print('Subtraction of numbers are:', num1 - num2)

    elif op == '/':
        if num2 == 0:
            print('Error: Division by zero')
        else:
            print('Division of numbers are:', num1 / num2)

    elif op == '%':
        if num2 == 0:
            print('Error: Modulo by zero')
        else:
            print('Modulo of numbers are:', num1 % num2)

    elif op == '//':
        if num2 == 0:
            print('Error: Floor division by zero')
        else:
            print('Floor division of numbers are:', num1 // num2)

    elif op == '**':
        print('Exponent of numbers are:', num1 ** num2)

    elif op == '*':
        print('Multiplication of numbers are:', num1 * num2)

    else:
        print('Invalid Input by user')

    continue_input = input('Do you want to continue? (yes/no): ')

    if continue_input == 'no':
        break


