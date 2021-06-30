bar_length = 20
current_number = 50
total_numb = 100

if (total_numb%10)==0:
    loaded_part = current_number/total_numb
    remaining_part = (total_numb-current_number)/total_numb
    loaded_length = loaded_part * bar_length
    remaining_length = remaining_part * bar_length

    loaded = '=' * (round(loaded_length)-1)
    remaining = ' ' * round(remaining_length)
    print(f'|{loaded}>{remaining}|')
else:
    print('Total_numb is not divisible by 10')