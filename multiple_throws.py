# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:20:19 2021

@author: Inger Lise
"""

import numpy as np

import math

throws = np.array([[40, 53], [53, 18], [2,3]])


angle = throws[0]
velocity = throws[1]
throw_height = throws[2]

print(angle)
#angle = input('Please enter the angle in degrees: ')
#velocity = input('Please enter the velocity in km/h: ')
#throw_height = input('Please enter the throw height in meter(s): ')

throw_angle = np.radians(angle)

throw_velocity = velocity / 3.6

horizontal_velocity = throw_velocity * np.cos(throw_angle)

vertical_velocity = throw_velocity * np.sin(throw_angle)

ball_airtime = (vertical_velocity + np.sqrt((vertical_velocity ** 2) + 2 * 9.81 * throw_height)) / 9.81

throw_distance = horizontal_velocity * ball_airtime


print(throw_angle)
print(throw_velocity)
print(horizontal_velocity)
print(vertical_velocity)
print(ball_airtime)
print(throw_distance)

#print(f'Throw angle: {throw_angle:.2f}')

#print(f'Throw velocity: {throw_velocity:.2f}')

#print(f'Horizontal velocity: {horizontal_velocity:.2f}')

#print(f'Vertical velocity: {vertical_velocity:.2f}')

#print(f'Ball airtime: {ball_airtime:.2f}')

#print(f'Throw distance: {throw_distance:.2f}')