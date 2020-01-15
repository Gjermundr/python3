<<<<<<< HEAD
# km/h to m/s calculator

def kmh_to_ms(kmh):
    ms = int(kmh) / float(3.6)
    print(kmh, 'KM/H is ', ms, 'meters per second')

def ms_to_mkh(ms):
    kmh = int(ms) * float(3.6)
    print(ms, ' M/s is ', kmh, 'kilometers per hour.')

def cel_fahren_convertion(cel):
    fahr = cel * 9 / 5 + 32
    print(cel,'*C ','=',fahr,'*F')

def fahren_cel_convertion(fahr):
    celcius = (fahr - 32) * 5 / 9
    print(fhar,'*F ', '=', celcius,'*C')


user_in = input('Gjermunds CALCULATOR:\n(1) KM/H to M/S\n(2)M/S to KM/H\n(3)Celcius to Fahrenheit\n(4) Fahrenheit to Celcius')

if user_in == '1':
    in1 = input('Enter KM/H: ')
    kmh_to_ms(in1)
elif user_in == '2':
    in2 = input('Enter M/S: ')
    ms_to_mkh(in2)
elif user_in == '3':
    in3 = int(input('Celcius: '))
    cel_fahren_convertion(in3)
elif user_in == '4':
    in4 = int(input('Fahrenheit: '))
    fahren_cel_convertion(in4)


def fibo_numbers(fn):
    answer = fn -1 + fn -2
    return answer

print(fibo_numbers(10))
=======
### REMEMBER TO ADD THE PREVIOUS TASKS!

# n1 and n2 are the first two values in the fibonacci sequence
n1 = 0
n2 = 1

# range(10) sets how many fibonacci sequences to be printed
for i in range(10):
    nx = n1 + n2
    print(nx)
# updating the two values before looping and printing the next value in the seq
    n1 = n2
    n2 = nx
>>>>>>> 8552e36a1bdc8c8a1b4e86e2f55ddf1d73ffde22
