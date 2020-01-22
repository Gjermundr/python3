import random
import time
# program that thinks of a number between 0 - 100, user tries to guess the number.
print('\n  Welcome to my mini-game!\n', '-'* 27, '\nTry to guess the randomly generated number from this program.\n If you guess wrong, a new number will be generated between\n your guess and the programs number untill you guess correctly.')
print('-'* 30,'\n')
#establishing some variables
guess = 0
answer = 1
low_range = 0
high_range = 1000
while guess != answer:
    guess = int(input('Make a guess between {} and {}: '.format(low_range, high_range)))
    while guess < low_range or guess > high_range:
        guess = int(input('Make a guess between {} and {}: '.format(low_range, high_range)))
    answer = random.randrange(low_range,high_range)
    print('You: ', guess, '; Program: ', answer)
    if guess == answer:
        print(r'''Winner Winner Chicken Dinner! <3
            _____________
            |  HIGHSCORE |
            |(1) Hoffnarr|
            |(2) Hoffnarr|
            |(3) Jerry   |
            --------------
              .___.
             /     \
            | O _ O |
            /  \_/  \
          .' /     \ `.
         / _|       |_ \
        (_/ |       | \_)
            \       /
           __\_>-<_/__
           ~;/     \;~
        ''')
        time.sleep(20)
# updates high and low range of game.
    elif guess < answer:
        low_range = guess
    elif guess > answer:
        high_range = guess