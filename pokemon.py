# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:56:15 2021

@author: Inger Lise
"""

captured = ('Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey')

print(captured)

print(captured.count('Pidgey'))

captured_set = set(['Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey'])

print(captured_set)

captured_check = input('Please enter the name of a Pokemon: ')

if captured_check in captured_set:
    print('Captured')
    print(captured.count(captured_check))
    print(captured_set.count(captured_check))
else:
    print('Not captured')
    

    