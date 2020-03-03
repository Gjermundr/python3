#  Ex1: modify the string
string = '''
Twinkle, twinkle, little star,
\t\tHow I wonder what you are!
\t\t\tUp above the world so high,
\t\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\t\tHow I wonder what you are
'''
print(string)

# Ex2: print python version in use
import sys
print('Python version')
print(sys.version)
print('Version info')
print(sys.version_info)


# Ex3: print the day
import datetime
print('Current date and time:')
date = str(datetime.datetime.today())
print(date[:-7])


# Ex4: calculate the area of user input
import math
def circle_area():
    r = float(input('Enter radius: '))
    area = math.pi * (r**2)
    print(f'area of {r} =', area)


circle_area()


# Ex5: get user's name and last name, then print it in reverse
def reverse_string():
    name = input('Enter full name: ')
    list = name.split(' ')
    i = len(list)
    for _ in list:
        i -= 1
        print('reversed: ',list[i], end=' ')
    print()


reverse_string()


# Ex6: accept a sequence of comma-separated numbers and generate a list and tuple with those numbers
num = input('Enter a sequence of numbers separated by commas\n:')
vals = num.split(',')
l1 = list(vals)
t1 = tuple(vals)
print('List: ', l1)
print('Tuple: ', t1)


# Ex7: accept a filename from user and print the extension of that file
file = input('Enter full filename: ')
ext = file[file.find('.'):]
print('file extension: ', ext)


# Ex8: display the first and last colors from the following list
color_list = ['Red', 'Green', 'White', 'Black']
print('First: ', color_list[0], '\nLast: ', color_list[-1])


# Ex9: Extract and display date
exam_st_date = (11, 12, 2014)
print(f'the examination will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}')

# Ex10: accept an int (n) from user and computes the value of n+nn+nnn
def f1():
    n = input('Enter an integer: ')
    n1, n2, n3 = n, n+n, n+n+n
    result = int(n1) + int(n2) + int(n3)
    print(n, ': n+nn+nnn =', result)


f1()


# Ex11: Write a program that print the documents of Python built-in functions (syntax, description etc.)
import types

def help_func():
    condition = True
    while condition:
        func = input('Enter a function name of type built-in: ')
        try:
            if isinstance(eval(func), types.BuiltinFunctionType):
                print(help(eval(func)))
                condition = False

            else:
                print('Function name not of type: Built-in, try again')
        except:
            pass


# help_func()

# Ex12: program to print the calendar of a given month and year
import calendar
def get_calender():
    cal = calendar.TextCalendar()
    year = int(input('Enter year:'))
    month = int(input('Enter month: '))
    cal.prmonth(year, month)


# get_calender()


# Ex14: print the diff between two dates.
import datetime

def date_diff():
    print('Enter two dates to calculate the difference in time off; Use format YYYY,M,D')
    f_date = input('Enter a date for which to calculate from: ')
    l_date = input('Enter a date for which to calculate to: ')
    l_fd = f_date.split(',')
    l_ld = l_date.split(',')
    date1 = datetime.datetime(int(l_fd[0]), int(l_fd[1]), int(l_fd[2]))
    date2 = datetime.datetime(int(l_ld[0]), int(l_ld[1]), int(l_ld[2]))
    print('Time difference: ', date2-date1)


# date_diff()



# Ex15: Python program to get the volume of a sphere with radius 6
import math
def sphere_volume(r):
    volume = ((r**3)/3) * 4 * math.pi
    print(volume)


sphere_volume(2)


# Ex16: get the difference between a given number and 17, if the number is greater than 17 return double the difference

def grow_diff(val: int):
    if val <= 17:
        print(17 - val)

    elif val > 17:
        print((val - 17) * 2)


grow_diff(11)








