# Hangman-Test
## ask_letter method
- Called the ask letter method in the play_game function to start the game.
- Asked the user for an input.
- Checked the input to make sure it's a valid letter.

## Initialising the attributes
- Initialised the attributes in the docstring (word_list, num_lives).
- Changed the random word to a list of "_" to hide it from the user.
- Printed out the length of the mystery word and the hidden word.

## check_letter method
- Called the check_letter method in the ask_letter method.
- Checks to see if the letter is in the word; if so, ammends the hidden word to display all occurences of that letter and reduces the number of unique letters remianing by the number of occurences; if not, reduces lives by 1.

## Game function
- Created a loop to continuously ask the user for input.
- Added win/lose messages upon reaching either zero lives or zero unique characters remaining in the mystery word.
