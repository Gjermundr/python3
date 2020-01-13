# testing the modulus operator: a % b = remainder of cycle
# think of modulus as a mother handing out an equal amount of candy to her kids. when the candy (a) left is not equal to the amount of kids (b), the modulus is the amount of candy left.
print(10 % 5, 7 % 6, 132 % 100, 9 % 2, 99 % 22)

userinput = input('Give me a number between 1 and 999999999999999999999999: ')
if int(userinput) % 2 == 0:
    print(str(userinput)+' is an even number.')

else:
    print(str(userinput)+' is an odd number.')