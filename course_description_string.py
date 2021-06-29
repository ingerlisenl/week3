
f_name = input('What is your first name?: ')
l_name = input('What is your last name?: ')
course = input('What is the name of your course?: ')
student_number = input('How many students are on your course?: ')



print('My name is', end= ' ')
print(f_name, end= ' ')
print('with last name', end= ' ')
print(l_name,'.')
print('I am participating in the course', end= ' ')
print(course, end=  ' ')
print('There are', end= ' ')
print(student_number, end= ' ')
print('candidates on the course.')

print(f'My name is {f_name.title()} with last name {l_name.title()}. I am participating in the course {course.lower()}. There are {student_number} candidates on the course.')