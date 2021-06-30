# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:14:19 2021

@author: Inger Lise
"""

while True:
    import random
    
    dice = [1,2,3,4,5,6]

    n_dice = 5

    rand_dice = random.choices(dice, k = n_dice)
    yatzee = rand_dice[0]==rand_dice[1]==rand_dice[2]==rand_dice[3]==rand_dice[4]
    print(rand_dice)
    
    if yatzee:
        print('Yatzee!')
        sort_dice = sorted(rand_dice)
        print(max(sort_dice))
        print(min(sort_dice))
        break
    else:
       print('Try again!')


