import random
import sys

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'CASA', 'CARRO', 'MONO', 'ESTERNOCLEIDOMASTOIDEO', 'PYTHON', 'DJANGO',
    'MILTON', 'LENIS', 'SWAPPS', 'LOGIA', 'UNITTESTING'
]

class Hangman():
    """
    The hangman game class with his methods
    """

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.word_to_guess = word_to_guess
        self.game_progress = ['_'] * len(self.word_to_guess)
        self.guessed_letters = set()

    def find_indexes(self, letter):
        """
        Method that takes a letter and returns a list with his indexes in
        the word to guess
        :param letter: String, Letter to find his indexes
        """
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]
    
    def is_valid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter 
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)
    
    def print_game_status(self):
        """
        Method to print the word to guess blankspaces with the remaining attempts and guessed letters.
        """
        # We append withespaces both sides to make the game look prettier
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_progress(self, letter, indexes):
        """
        Method to update the game progress with guessed letters
        :param letter: String, letter to be added to the game progress
        :param indexes: List, found occurrences (as indexes) of the given letter in the word
        """

        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nPlease type a letter: ')
        return user_input.upper()

    def play(self):
        """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """

        while self.failed_attempts < len(HANGMAN):
            self.print_game_status()
            user_input = self.get_user_input()

            #Validate the user input
            if self.is_valid_letter(user_input):
                print('¡The input is not a letter!')
                continue

            if user_input in self.guessed_letters:
                print('You already have guessed that letter!')
                print(self.guessed_letters)
                continue
            
            self.guessed_letters.add(user_input)
            print(self.guessed_letters)

            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                #if there is no letter to find in the word
                if '_' not in self.game_progress:
                    print('\n¡Yay! You win!');
                    print('The word is {0}'.format(self.word_to_guess))
                    sys.exit()

            else:
                self.failed_attempts += 1
        print("\n¡OMG! You lost!")
        
word_to_guess = random.choice(WORDS)
hangman = Hangman(word_to_guess)
hangman.play()