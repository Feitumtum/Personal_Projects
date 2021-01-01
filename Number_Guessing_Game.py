#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is
#within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"

#On all subsequent turns, if a guess is
#closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"

#When the player's guess equals the number, tell them they've guessed correctly
#and how many guesses it took!
from random import randint

game = True
num = randint(0, 101)
counter = 0
guess_list = []
print('Play the Guessing Game!')

while game:
    print()
    guess = int(input('Guess a number from 0 to 100: '))
    guess_list.append(guess)
    counter = counter + 1

# out of bounds guess
    if guess > 100 or guess < 0:
        print('Guess is out of bounds')
        last_guess = guess
        continue
    
# first guess indicator
    if counter == 1:
        if abs(guess - num) <= 10:
            print('WARM')
        else:
            print('COLD')
        last_guess = guess
        continue

    if guess == num:
        game = False


    if guess != num:
        if abs(guess-num) < abs(last_guess-num):
            print('Wrong, but WARMER')
        else:
            print('Wrong and COLDER')
        last_guess = guess

print(f'Correct! You took {counter} number of guesses')
print(f' You guesses {guess_list}')
