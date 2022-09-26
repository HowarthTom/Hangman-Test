import random
import string

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).upper()
        self.num_letters = len(self.word)
        self.word_guessed = ["_" for characters in self.word]
        self.num_lives = num_lives
        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")
        pass

    def check_letter(self, letter):
        pass

    def ask_letter(self):
        letter = input("Guess a letter: ").upper()
        if len(letter) > 1:
            print("Please, enter just one character.")
        elif letter not in string.ascii_letters:
            print("Please, enter a valid character.")
        else:
            print(f"Thanks, you entered the letter {letter}")
    
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)