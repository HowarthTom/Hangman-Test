import random
import string

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).upper()
        self.num_letters = len(self.word)
        self.word_guessed = ["_" for characters in self.word]
        self.num_lives = num_lives
        self.list_letters = []
        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")

    def check_letter(self, letter):
        self.list_letters.append(letter)
        if letter not in self.word:
            self.num_lives -= 1
            print(f"Bad luck! {letter} was not in the word. {self.num_lives} lives remaining")
        else:
            for character in range(len(self.word)):
                if self.word[character] == letter:
                    self.word_guessed[character] = letter
                    self.num_letters -= 1
                else:
                    continue

    def ask_letter(self):
        letter = input("Guess a letter: ").upper()
        if len(letter) > 1:
            print("Please, enter just one character.")
        elif letter not in string.ascii_letters:
            print("Please, enter a valid character.")
        elif letter in self.list_letters:
            print(f"{letter} was already tried. Letters used: {self.list_letters}")
        else:
            self.check_letter(letter)
    
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)