num_1 = input('Please choose a number: ')
operator = input('Please choose an operator: ')
num_2 = input('Please choose another number: ')



if num_1.isnumeric()  and num_2.isnumeric():
    if operator == '+':
        add_sum = float(num_1) + float(num_2)
        print(f'{num_1} + {num_2} = {add_sum}')
    
    elif operator == '/':
        if num_2 == '0':
            print('Sorry, a number can not be divided by zero')
        else:
            div_sum = float(num_1) / float(num_2)
            print(f'{num_1} / {num_2} = {div_sum}')

    elif operator == '-':
        sub_sum = float(num_1) - float(num_2)
        print(f'{num_1} - {num_2} = {sub_sum}')
    
    elif operator == '*':
        mul_sum = float(num_1) * float(num_2)
        print(f'{num_1} * {num_2} = {mul_sum}')

    else: 
        print('Please run program again and choose a valid operator')
else: 
    print('Please run program again and choose valid numbers')
