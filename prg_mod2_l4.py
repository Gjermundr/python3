list = []
for i in range(101):
    list.append(i)
print(list)

# for loop to print every even number in the list: list
for even in list:
    if even % 2 == 0:   # Checks every iteration in list, prints only integers that evaluates to zero
        print(even)


key_list = []
value_list = []
dictonary = {
    'a':'Alpha','b':'Beta','c':'Charlie','d':'Delta','e':'Echo','f':'Foxtrot','g':'Golf','h':'hotell','i':'India',
    'j':'Juliet','k':'Kilo','l':'Lima','m':'Mike','n':'November','o':'Oscar','p':'Papa','q':'Quebec','r':'Romeo',
    's':'Sierra','t':'Tango','u':'Uniform','v':'Victor','w':'Wisky','x':'X-ray','y':'Yankee','z':'Zulu'
}

# Add all values and keys to separate lists.
for value in dictonary.values():
    value_list.append(value)

for key in dictonary.keys():
    key_list.append(key)


value_list.sort()
key_list.sort()

print(value_list,'\n',key_list)

for i in value_list:
    print(i)

# make a program that counts the occurrence of a spesific letter in a word or sentence
def split(word):
    return [char for char in word]

#data = input('Enter the data to be analyzed: ')
letter = input('Enter the letter: ')
data = 'super duper uber penis kuk face faggot faen helvette altsåm, dette gjidder jeg ikke lenger hehehehehehee morra'
print(split(data))

for letter in data:
   data.count(letter)
   print(letter)

