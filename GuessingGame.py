# File: GuessingGame.py
# Description of Program: Gets user input to guess a number (1458) in 10 guesses and tells if guess is too high, too low, correct, or invalid.


count = 0
print("Welcome to the guessing game. You have ten tries to guess my number.")
guess = input("Please enter your guess: ")
guess = int(guess.strip())
while guess <= 0 or guess >= 9999:
    print("Your guess must be between 0001 and 9999.")
    guess = int(input("Please enter a valid guess: "))
if guess == 1458:
    print("That's correct!")
    print("Congratulations! You guessed it on the first try!")
    
count += 1
def numberGuesses(guess): 
    for count in range(0,10):
        while guess <= 0 or guess >= 9999:
            print("Your guess must be between 0001 and 9999.")
            guess = int(input("Please enter a valid guess: "))
        count += 1
        if guess < 1458:
            print("Your guess is too low.")
        elif guess > 1458:
            print("Your guess is too high.")
        elif guess == 1458: 
            print("That's correct! \nCongratulations! You guessed it in", count, "guesses.")
            break
        if count == 10:
            print("Guesses so far:", count)
            print("Game over: you ran out of guesses.")
            break
        print("Guesses so far:", count)
        guess = input("Please enter your guess: ")
        guess = int(guess.strip())

if guess != 1458:
    numberGuesses(guess)       
    