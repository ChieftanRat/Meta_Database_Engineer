#Type casting input

# Using expliciting type conversion, changing the following
# inputs so the types match with the below:
# name = string
# age = int
# height = float
# loyalty = type boolean

name = input('What is your name? ')

print(f'Type of name variable is: {type(str(name))}')

age = input('What is your age? ')

print(f'Type of age variable is: {type(int(age))}')

height = input('What is your height in meters? ')

print(f'Type of height variable is: {type(float(height))}')

loyalty = input('Are you part of our loyalty program? ')

print(f'Type of loyalty variable is: {type(bool(loyalty))}')

