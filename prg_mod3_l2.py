# string manipulation
my_string = "asshat"
slice_of_string = my_string[1:4] # starting at index 1 to char before index 4
print(slice_of_string)

# escape character /
print('This is a test\t string, using escape \\ characters.\nPretty cool, right?')

# Raw strings = r
url = 'https://www.pornhub.com/'
print(url, r'or https://www.pornhub.com/')

# Formatted strings with placeholders, {}, f, .format()
my_second_string = '{} sold {} items.'
print(my_second_string.format('Jensen', 99))
print('This format {} is done on {} spot'.format('string','the'))

# easy program to tell you if a char or number is entered...
condition = True
user_in = input('Enter whatever: ')
while condition:                                            # while loop incase a special character is entered
    if user_in.isalpha():
        print(user_in,' is a character')
        condition = False
    elif user_in.isnumeric():
        print(user_in, ' is a number')
        condition = False
    elif not (user_in.isnumeric() and user_in.isalpha()):   # if input contains a speciial charater the user is corrected and asked again.
        print('dont use special characters please...')
        user_in = input('Enter whatever else: ')


# Program receiving numbers and letters, then determining the amount of numbers vs letters.
#user_input = input('Enter whatever you want: ')
#split_input = list(user_input)
#print(split_input)


def max(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

print(max(190,100))


def max_of_three(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3

print(max_of_three(100,12,1151))

def fibonacci_gen(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev = curr
        curr = prev + curr
        counter += 1

print(fibonacci_gen(10))





