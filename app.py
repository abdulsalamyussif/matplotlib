
while True:
    print('For conversion from Decimal to Binary, press 1: ')
    print('For conversion from Binary to Decimal, press 2: ')
    option = int(input('Enter 1 or 2: '))
    if option == 1:
        number = input('Enter Decimal to convert to Binary: ')
        number = int(number)
        convert_to_binary = bin(number)
        print(f'The Decimal form of the Binary number is:\n {convert_to_binary[2:]}')
    elif option == 2:
        number = input('Enter Binary to convert to Decimal: ')
        converter = int(number, 2)
        print(f'The result of the conversion to decimal is :\n {converter}')
        print()

    else:
        print('Please enter 1 or 2 for the conversion')
        break




