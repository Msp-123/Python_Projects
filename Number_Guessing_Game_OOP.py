import random
import math
import sys

class NumberGuessingGame:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
        self.number_to_guess = random.randint(lower, upper)
        self.number_of_guess = math.ceil(math.log2(upper - lower + 1))
        self.count = 0

    def ordinal(self, number):
        if 10 <= number % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
            return f"{number}{suffix}"

    def get_valid_input(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print('Please enter a valid integer.')

    def start_game(self):
        
        
        self.lower_bound = self.get_valid_input('Enter lower bound: ')
        self.upper_bound = self.get_valid_input('Enter upper bound: ')

        while self.lower_bound >= self.upper_bound:
            print('Upper bound must be greater than lower bound.')
            self.lower_bound = self.get_valid_input('Enter lower bound: ')
            self.upper_bound = self.get_valid_input('Enter upper bound: ')
            
        print('\n\tYou have only {} chances to guess the number!\n'.format(self.number_of_guess))

        while self.count < self.number_of_guess:
            self.count += 1
            self.make_guess()
            print("It was your {} try.".format(self.ordinal(self.count)))

        self.display_result()

    def make_guess(self):
        while True:
            user_input = input('Guess a number: ')
            if user_input.isdigit():
                user_guess = int(user_input)
                break
            else:
                print('Please enter a valid integer.')

        if self.number_to_guess == user_guess:
            print('Congratulations you did it in {} try'.format(self.count))
            sys.exit()
        elif self.number_to_guess > user_guess:
            print('Your guess is smaller than my number :) ')
        elif self.number_to_guess < user_guess:
            print('Your guess is bigger than my number :) ')

    def display_result(self):
        if self.count >= self.number_of_guess:
            print('\nThe number was {}.'.format(self.number_to_guess))
            print('\tBetter Luck Next Time!')

if __name__ == "__main__":
    game = NumberGuessingGame(0, 100)  # Default initial bounds
    game.start_game()
