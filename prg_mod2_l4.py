list = []
for i in range(101):
    list.append(i)
print(list)

# for loop to print every even number in the list: list
for even in list:
    if even % 2 == 0:   # Checks every itteration in list, prints only integers that evaluates to zero
        print(even)

