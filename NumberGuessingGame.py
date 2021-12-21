'''
This code was designed to complete a challenge for a Number Guessing Game. I attempted to pass any possible exceptions I could think of. Have fun guessing the correct number!
If needed, there are config variables too that can adjust maxGuesses, minNum, and maxNum.
Input: Integer Guess
Output: Results of if guess is correct or not. If not, explains why. Will also display a final end game result
Author: MadiSperry
'''

# Organize imports
import random

# Create validateGuess function to test guess
def validateGuess(lowestNum, highestNum, guess):
    # Test if the guess is actually numeric, if not, this is not valid
    if str(abs(int(guess))).isnumeric() == True:
        # Test if guessedNum is inbetween the restraints of lowestNum and highestNum, return result
        if int(guess) >= int(lowestNum) and int(guess) <= int(highestNum):
            return True    
        else:
            return False
    else:
        return False

# Config Variables
maxGuesses = 10
minNum = -100
maxNum = 100

# Create static variables that should not change
guessesUsed = 0
correctGuess = False

# Pulls a random number between minNum and maxNum
numberToGuess = int(random.randint(minNum, maxNum))

# Starts the first input request for a guess
guess = input("Let's play a game! I picked a number between " + str(minNum) + " and " + str(maxNum) + ". Guess what it is: ")

# Create loop to test guess until it is correct or the max tries is used
while correctGuess == False and guessesUsed < maxGuesses:
    # Increase the guessesUsed counter
    guessesUsed += 1

    # Use the validGuess function to test if the guess is a valid number between minNum and maxNum
    validGuess = validateGuess(minNum, maxNum, guess)
    
    # Condition for if the guess is not a valid number between 0 and 100
    if validGuess == False:
        guess = input("That is incorrect. The number is actually a numeric number between " + str(minNum) + " and " + str(maxNum) + ". You have " + str(maxGuesses - guessesUsed) + " guesses left. Try keeping you guess between 0 and 100: ")
    # Condition for if the number guessed is lower than the number to guess, ends the loop early
    elif int(guess) == numberToGuess:
        correctGuess = True
        continue
    # Condition for if the number guessed is higher than the number to guess
    elif int(guess) > numberToGuess:
        guess = input("That is incorrect. The number is lower than " + str(guess) + ". You have " + str(maxGuesses - guessesUsed) + " guesses left. What is you next guess: ")
    # Condition for if the number guessed is lower than the number to guess
    elif int(guess) < numberToGuess:
        guess = input("That is incorrect. The number is higher than " + str(guess) + ". You have " + str(maxGuesses - guessesUsed) + " guesses left. What is you next guess: ")


# Print end game results
if correctGuess == True:
    print("Congratulations! You guessed the number correctly in " + str(guessesUsed) + " guess(es).")
else:
    print("Sad day... You did not guess the correct number in all of the " + str(guessesUsed) + " guesses you used. It was " + str(numberToGuess))
