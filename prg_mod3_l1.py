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
