import random
name = input ('What is your name? ')
print ('Well ' + name + ', I am thinking of a number between 1 and 20.')

secret_number = random.randint(1, 20)

for guesses_taken in range (1,7):
    guessed_number = int(input('Take a guess. '))
    if guessed_number < secret_number:
        print ('That number is too low.')
    elif guessed_number > secret_number:
        print ('That number is too high.')
    else:
        print ('You guessed the right number!')
        break

if guessed_number != secret_number:
    print ('Nope the right answer is', secret_number,'.')

print ('You took', guesses_taken, 'guesses.')