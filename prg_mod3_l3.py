import random

class clothes:
    def __init__(self, type1, color, size):
        self.type1 = type1
        self.color = color
        self.size = size

    def fabric(self):
        print('Clothing: ', self.type1, 'Fabric: silk')

    def age(self):
        print('Clothing: ',self.type1, 'State: Worn')

    def display(self):
        print('Your Clothing Items: {}, {}, {}'.format(self.type1, self.color, self.size))

test_class = clothes('pants', 'red', '43')
test_class.fabric()
test_class.age()
test_class.display()


# program that thinks of a number between 0 - 100, user tries to guess the number.
print('\n  Welcome to my mini-game!\n', '-'* 27, '\nTry to guess the randomly generated number from this program.\n If you guess wrong, a new number will be generated between your guess and the programs number\n untill you guess correctly.')
#establishing some variables
guess = 1
answer = 1
low_range = 0
high_range = 1000
while guess != answer:
    guess = int(input('Make a guess between {} and {}'.format(low_range, high_range)))
    while guess < low_range or guess > high_range:
        guess = int(input('Make a guess between {} and {}'.format(low_range, high_range)))
    answer = random.randrange(low_range,high_range)
    print('Your guess: ', guess, 'Program: ', answer)
    if guess == answer:
        print('Winner Winner Chicken Dinner!')
# updates high and low range of game.
    elif guess < answer:
        low_range = guess
    elif guess > answer:
        high_range = guess

# calculator that finds the hypotenus and angels in a triangle.

side_A = int(input('Side A: '))
side_B = int(input('Side B: '))
hypotenus_c = (side_A * side_B) / 2

angle_x = 90
angle_y = (180 - angle_x) / 2
angle_z = (180 - angle_x) / 2
print(angle_x, angle_y, angle_z)