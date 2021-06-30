# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 15:32:28 2021

@author: Inger Lise
"""


def bart (punishment_text, numb_of_repetition=10):
    print(punishment_text * numb_of_repetition)
    counted = punishment_text.count('that')
    print(f'The number of the word THAT in the original sentence is: {counted}')
    
bart('hello that that that')