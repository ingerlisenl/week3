import math

angle = input('Please enter the angle in degrees: ')
velocity = input('Please enter the velocity in km/h: ')
throw_height = input('Please enter the throw height in meter(s): ')

throw_angle = math.radians(float(angle))

throw_velocity = float(velocity) / 3.6

horizontal_velocity = throw_velocity * math.cos(throw_angle)

vertical_velocity = throw_velocity * math.sin(throw_angle)

ball_airtime = (vertical_velocity + math.sqrt(math.pow(vertical_velocity, 2) + 2 * 9.81 * float(throw_height))) / 9.81

throw_distance = horizontal_velocity * ball_airtime



print(f'Throw angle: {throw_angle:.2f}')

print(f'Throw velocity: {throw_velocity:.2f}')

print(f'Horizontal velocity: {horizontal_velocity:.2f}')

print(f'Vertical velocity: {vertical_velocity:.2f}')

print(f'Ball airtime: {ball_airtime:.2f}')

print(f'Throw distance: {throw_distance:.2f}')



