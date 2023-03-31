"""Rock Paper Scissors"""

import random
import os # This module provides a portable way of using operating system dependent functionality
import re # This module provides regular expression matching operations similar to those found in Perl.

def check_play_status():
    valid_responses = ['yes', 'no']   
    while True:
        try:
            response = input('Do you wish to play again? (ONLY Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('ONLY yes or no')
                
            elif response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name =='nt' else 'clear') # windows cls ==  clear in Linux
                print('Thanks for playing')
                exit()
            
        except ValueError as Error:
            print(Error)

def play_rps():
    play=True
    while play:
        os.system('cls' if os.name =='nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - Shoot!')
        
        user_choice = input('Choose your weapon [R]ock, [P]aper, or [S]cissors:')
        user_choice = user_choice.upper()
        
        if not re.match("[SsRrPp]", user_choice):
            print('Please choose your weapon by using a letter')
            print('[R]ock, [P]aper, or [S]cissors')
            continue
        
        print(f'Your weappn: {user_choice}')
        
        choices = ['R', 'S', 'P']
        computer_choice = random.choice(choices)
        
        print(f'I chose: {computer_choice}')
        
        if computer_choice == user_choice:
            print('Tie')
        elif computer_choice == 'R' and user_choice == 'S':
            print('Rock beats scissors, I win!')
            play = check_play_status()
        elif computer_choice == 'S' and user_choice == 'P':
            print('Scissors beats paper! I win!')
            play = check_play_status()
        elif computer_choice == 'P' and user_choice == 'R':
            print('Paper beats rock, I win!')
            play = check_play_status()
        else:
            print('You win\n')
            play = check_play_status()
        
if __name__ == '__main__':
    play_rps()        