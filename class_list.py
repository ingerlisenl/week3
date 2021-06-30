# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:53:26 2021

@author: Inger Lise
"""
class_list = ['Jacob Wang', 'Abderrahman Amsalkhir', 'Kari Jonassen', 'Fredrik Lyford', 'Nelly Askjer']

print(class_list)

print(class_list[2])
print(class_list[2][0])

class_list[2] = 'Ole'
print(class_list)

class_list[2] = 'Ole Nordmann'
print(class_list)

class_list.append('Kari Jonassen')
print(class_list)

class_list.insert(4, 'Monty Python')
print(class_list)

class_list.remove('Ole Nordmann')
print(class_list)

print(class_list.index('Monty Python'))

print(class_list[0:3])

class_reverse = class_list[::-1]
print(class_reverse)

class_even = class_list[1::2]
print(class_even)

class_odd = class_list[::2]
print(class_odd)