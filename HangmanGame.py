'''
This code was designed to complete a challenge for a Hangman game. The only possible inputs are alpha characters, all else will not affect code. Enjoy a game of guess the characters! 
Input: Alpha Character Guess
Output: Hangman picture, word/phrase category, Incorrectly guessed letters, correct guesses in spaces, and end game result
Author: MadiSperry
'''

# Organize imports
import os
from random import randint

# Define function to check if the guess is valid, if valid, it will let return a list of each position of the hidden word to reveal or either "Incorrect" or "Invalid"
def checkGuess(wordToGuess, hiddenWord, guessedChar):
    # Check if the guessedChar is in wordToGuess, an alpha character, and only 1 character long, if so, it is correct and return each index of the word that it is correct in. If it is an alpha character 
      # and it is only 1 character long, it is incorrect. Any other input is invalid.
    if guessedChar in wordToGuess and guessedChar.isalpha() and len(guessedChar) == 1:
        correctLetterIndex = [i for i in range(len(wordToGuess)) if wordToGuess.startswith(guessedChar, i)]
        return correctLetterIndex
    elif guessedChar.isalpha() and len(guessedChar) == 1:
        return "Incorrect"
    else:
        return "Invalid"

# Define function to clear terminal completely
def clearTerminal():
    os.system('cls||clear')

# Define function to display the hangman picture and all associated text
def displayHangman(misses, hiddenWord, category, guessedLettersList):
    # Create empty string to be overriden with joined list
    guessedLetters = ""
    guessedLetters = guessedLetters.join(guessedLettersList)

    # Create list for guessed letters with space in between
    guessedLettersList = [char + " " for char in guessedLetters]

    # Wipe the guessedLetters string to be reoverriden with joined list again
    guessedLetters = ""
    guessedLetters = guessedLetters.join(guessedLettersList)

    # Run clearTerminal function
    clearTerminal()

    # Display the hangman picture with characters based off how many times the player has entered in a wrong letter
    if misses == 0:
        print("     ___")
        print("    |  | ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif misses == 1:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    |    ")
        print("    |    ")
        print("    |    ")
        print("____|____")
    elif misses == 2:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    |  | ")
        print("    |  | ")
        print("    |    ")
        print("____|____")
    elif misses == 3:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    | /| ")
        print("    |  | ")
        print("    |    ")
        print("____|____")
    elif misses == 4:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    | /|\\")
        print("    |  | ")
        print("    |    ")
        print("____|____")
    elif misses == 5:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    | /|\\")
        print("    |  | ")
        print("    | /  ")
        print("____|____")
    elif misses == 6:
        print("     ___")
        print("    |  | ")
        print("    |  O ")
        print("    | /|\\")
        print("    |  | ")
        print("    | / \\")
        print("____|____")

    # Print Hidden Word's category, the incorrectly guessed letters, and the word still containing "_" or completed word
    print("\nCategory: " + category + "\n\nIncorrectly Guessed Letters: " + guessedLetters + "\n\n\n" + hiddenWord)

# Define function to generate and return a word with "_" and " " from given word
def generateHiddenWord(word):
    # Create a hidden word by creating a list for each character being "_ " and each space being "  ".
    hiddenWordListed = ["_ " if char != " " else "  " for char in word]
    
    # Create an empty variable to be overriden with the string of the hiddenWordListed list with no spaces before or after.
    hiddenWord = ""
    hiddenWord = hiddenWord.join(hiddenWordListed).strip()

    # Return result
    return hiddenWord

# Define function to generate and return a word from a given category
def generateWord(category):
    # Create lists for the different categories
    superHeros =        ["BATMAN", "BATWOMAN", "SUPERMAN", "SUPERGIRL", "GREEN ARROW", "GREEN LANTERN", "WONDER WOMAN", "AQUAMAN", "BLACK CANARY", "SHAZAM", "FIRESTORM"
                         "IRON MAN", "HULK", "SPIDERMAN", "DOCTOR STRANGE", "BLACK WIDOW", "BLACK PANTHER", "CAPTAIN AMERICA", "THOR", "DEADPOOL", "SCARLET WITCH", "HAWKEYE"]
    altMusicArtists =   ["TWENTY ONE PILOTS", "MY CHEMICAL ROMANCE", "PANIC AT THE DISCO", "FALL OUT BOY", "GREEN DAY", "WEEZER", "ARCTIC MONKEYS", "RED HOT CHILI PEPPERS",
                         "THE SMASHING PUMPKINS", "THE KILLERS", "NIRVANA", "FOO FIGHTERS", "NINE INCH NAILS", "LINKIN PARK", "THE WHITE STRIPES", "PARAMORE"]

    # Choose a word from the selected category
    if category == "Super Heros":
        chosenWord = superHeros[randint(1, len(superHeros)) - 1]
    elif category == "Alternative Music Artists":
        chosenWord = altMusicArtists[randint(1, len(altMusicArtists)) - 1]
    
    # Return result
    return chosenWord

# Define function to pick and return a category for use in other functions
def pickCategory():
    # Create a list with strings of different category names
    categories = ["Super Heros", "Alternative Music Artists"]
    
    # Choose a category from the above list
    chosenCategory = categories[randint(1, len(categories)) - 1]

    # Return result
    return chosenCategory

# Define function to replace "_" in hiddenWord with guessedChar and return the result
def replaceLetters(correctLetterIndex, hiddenWord, guessedChar):
    # Create variables
    indexCounter = 0
    
    # Create a new list from hiddenWord that seperates each character into a list item
    newHiddenWordList = [char for char in hiddenWord]

    # Create for loop that tests each index in the list        
    for index in range(len(newHiddenWordList)):
        # If the index character is not a space and the indexCounter is a number in the correctLetterIndex list, replace that "_" with the guessedChar and add 1 to indexCounter
        if newHiddenWordList[index] != " " and indexCounter in correctLetterIndex:
            newHiddenWordList[index] = guessedChar
            indexCounter += 1
        # If there are 3 spaces in a row, which only happens when there is a space between the differnt words, add 1 to indexCounter
        elif newHiddenWordList[index - 1] == " " and newHiddenWordList[index] == " " and newHiddenWordList[index + 1] == " ":
            indexCounter += 1
        # If the index character is not a space and the indexCounter is not a number in the correctLetterIndex list, add 1 to indexCounter
        elif newHiddenWordList[index] != " " and indexCounter not in correctLetterIndex:
            indexCounter += 1
            
    # Reset the newHiddenWord to a blank string, then create a string out of the newHiddenWordList
    newHiddenWord = ""
    newHiddenWord = newHiddenWord.join(newHiddenWordList)

    # Return result
    return newHiddenWord

#############################################################################################################################################################################################################

# Define function to run main part of script
def main():
    # Choose category and add to variable category
    category = pickCategory()
    # Choose word from category and add word to wordToGuess
    wordToGuess = generateWord(category)
    # Convert wordToGuess to a string of only "_" and " "
    hiddenWord = generateHiddenWord(wordToGuess)

    # Create other variables
    misses = 0
    guesses = []

    # Create a loop that until the cx reaches total completion or 6 misses, will start off by displaying the hangman game in terminal
    while misses < 6 and "_" in hiddenWord:
        displayHangman(misses, hiddenWord, category, guesses)

        # Take input from player for their guess
        guess = input("\nGuess a Letter: ").upper()

        # Check the guess to see if it is correct, incorrect, or invalid
        checkedGuess = checkGuess(wordToGuess, hiddenWord, guess)
        # Based off above result, if guess is correct, replace the letters in hiddenWord, else if the entry is invalid, do nothing, 
          # else if the guess is incorrect and hasn't been guessed before, add guess to guesses list, sort list, and 1 to total misses
        if checkedGuess != "Incorrect" and checkedGuess != "Invalid":
            hiddenWord = replaceLetters(checkedGuess, hiddenWord, guess)
        elif checkedGuess == "Invalid":
            continue
        elif guess not in guesses:
            guesses += [guess]
            guesses.sort()
            misses += 1
    
    # Display end game results
    displayHangman(misses, hiddenWord, category, guesses)
    # Decides if win or lose based off how many misses the player has
    if misses < 6:
        print("\nCongratulations! You guessed the word " + wordToGuess + " correctly!")
    else:
        print("\nBetter luck next time! The word was " + wordToGuess + ".")

#############################################################################################################################################################################################################

# Run the main function
main()