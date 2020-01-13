# testing the modulus operator: a % b = remainder of cycle
# think of modulus as a mother handing out an equal amount of candy to her kids. when the candy (a) left is not equal to the amount of kids (b), the modulus is the amount of candy left.
print(10 % 5, 7 % 6, 132 % 100, 9 % 2, 99 % 22)

userinput = input('Give me a number between 1 and 999999999999999999999999: ')
if int(userinput) % 2 == 0:
    print(str(userinput)+' is an even number.')

else:
    print(str(userinput)+' is an odd number.')

# lists, arrays, and whatever... syntax: list_var = [1,2,3,4.78,'etc']
#                                         list index: 0,1,2,3,4,5,6
# Methods: .Methodname()
# int_list.append(val) // append value to the end of list
# int_list.insert(index, value) // insert a value and extend the list by 1
# int_list.extend(val) // add the contents of an entire other list to the end of a list.
# int_list.remove(val) // removes the first occurence of the value
# del(int_list[val]) // remove a spesific item from a list
# int_list.pop(index) // returns the value stored at the index and then removes the item from the list

## Manipulating lists
# int_list[start:stop:step] // start= first index to select, stop= selects the end of the slice of the trailing index. step= 1=every index, 2= every other index... etc
int_list = [12, 2, 43, 125, 64, 1, 66]
print(int_list[0:5:2])
int_list2 = [421, 5, 1531, 63, 1, 664, 3]
int_list2.append(100000)
int_list.insert(1, 99)
print(int_list)
print(int_list[0:3])

## Tuples .. immutable lists that can not be changed once created.
int_tuple = (1, 2, 3, 4, 5)
a, b, c, d, e = int_tuple
print(a, b, e)

## Set

color_set = {'black', 'white', 'grey', 'orange', 'orangutang'}
print(color_set)

# add a string to the set
color_set.add('purple')
print(color_set)

# discard a value from the set
color_set.discard('white')
print(color_set)

# .intersection() to determine which values appear in 2 sets
other_set = {'adamantium', 'greencush', 'black', 'orange'}
print(other_set)
print('intersecting shits in two sets:', color_set.intersection(other_set))

# use .difference() to determine which values appear in the first set, but not in the second
print('the diff of the two sets: ', color_set.difference(other_set))

## Dictionaries .. dictionary_list {key:value, key:value, key:value}
salesperson_sales = {'Tom': 1234, 'vegard': 4321, 'bv': 1337}
print('customers list dictionary: ', salesperson_sales)

# get only corresponding value to key:
print('bv\'s sales: ', salesperson_sales['bv'])
# fuck tom, han skal ut
del (salesperson_sales['Tom'])
# print only the keys without value
print('print only the keys: ', salesperson_sales.keys())

### PRAX
# Activity 1
ac1_list = ['python', 'c', 'java']
print('here you have index 0 of the list: ', ac1_list[0])
print(ac1_list[1], 'is an old programming language...')
print('fuck ', ac1_list[2])

# Activity 2
career_list = ['programmer', 'truck driver', 'teacher', 'professional pedophile', 'pornstar']
print(career_list.index('teacher'))
career_list.append('hacker')
career_list.insert(0, 'bill gates')
print('hacker' in career_list)
print(career_list)
i = 0
while i < 5:
    print(career_list[i])
    i += 1

gen_list = []
i = 0
while i <= 20:
    gen_list.append(i)
    print(gen_list[i])
    i += 1


odd_list = []
x = 0
if x % 2 == 1:
    odd_list.append(x)

print(odd_list)

