# shopping list program, the program exits when the user enters 'done'
testlist = []
add_item = input('Shopping list: When finished, enter "done"\nWhat would you like to add: ')
testlist.append(add_item)
while add_item != 'done':
    add_item = input('What would you like to add: ')
    testlist.append(add_item)
if add_item == 'done':
    testlist.remove('done')
    print(testlist)


from typing import Any, Union
# a list
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'Desember']


for m in months:
    print(m[0])

months.sort()

print(months)


# a tuple
rainbow = ('Red', 'Blue', 'Green', 'Orange', 'Violet', 'Yellow', 'Indigo')
print(rainbow)

# a set
fruit1 = {'apples', 'oranges','bananas'}
fruit2 = {'kiwis', 'apples', 'grapes'}

print(fruit1, fruit2)


# dictonary with keys
person_data = {'Name':'', 'Street':'', 'zip-code':'', 'Phone':'', 'Email':''}
# prompt user for information
print('Please enter your personal information down below!')
name = input('What is your name: ')
street = input('Street name: ')
zip = input('zip-code: ')
phonenr = input('Phone number: ')
email = input('Email address: ')

# add the new data to the dictionary
person_data['Name'] = name
person_data['Street'] = street
person_data['zip-code'] = zip
person_data['Phone'] = phonenr
person_data['Email'] = email

print(person_data)