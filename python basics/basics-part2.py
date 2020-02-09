# Ex1: take a sequence of numbers and determine wether all the numbers are different from each other.
def distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(distinct([1,2,6,3,7]))
print(distinct([1,5,1,4,6,4]))


# Ex2: program that create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use characters only once.
def all_itterations(letters):
    for l in letters:
        for i in range(len(letters)):
            letters.insert(i, l)
            print(letters)

print(range(len(['a', 'e', 'i', 'o', 'u'])))
# all_itterations(['a', 'e', 'i', 'o', 'u'])