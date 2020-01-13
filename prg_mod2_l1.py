# Task 1: make program to prompt user for a number between 0 - 100
'''
number = input('Give me a number between 0 to 100: ')

if int(number) > 100 or int(number) < 0:
    print('The number is not within the given range. Try again!')
else:
    print('Correct!')

'''
# Task 2: pH calculator - print the acid that corresponds to the value given.
user_value = float(input('Give me a value between 0.0 - 14.0: \n'))

while user_value > float(14.0):
    print('The value is not within range! Please try again...\n')
    user_value = float(input('Give me a value between 0.0 - 14.0: \n'))



def ph_calc(ph_value):
    if ph_value >= 0.0 and ph_value <= 6.5:
        return print(ph_value, ' is acidic')
    elif ph_value >= 6.6 and ph_value <= 7.3:
        return print(ph_value, ' is normal')
    elif ph_value >= 7.4 and ph_value <= 14.0:
        return print(ph_value, ' is alkaline')


ph_calc(user_value)

