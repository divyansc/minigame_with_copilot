import random


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_player_choice():
    player_input = input('Enter your choice: (rock,paper or scissors)').lower()
    while player_input not in ['rock', 'paper', 'scissors']:
        player_input = input('Invalid choice. Please enter the valid choice: (rock,paper or scissor)').lower()
    return player_input

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        return 'player'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        return 'player'
    elif player_choice == 'paper' and computer_choice == 'rock':
        return 'player'
    else:
        return 'computer'

def play_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        computer_choice = get_computer_choice()
        player_choice = get_player_choice()
        print(f'Computer choice: {computer_choice}')
        print(f'Player choice: {player_choice}')
        winner = get_winner(player_choice, computer_choice)
        if winner == 'draw':
            print('It is a tie')
        elif winner == 'player':
            player_score += 1
            print(' You wins this round!!')
        else:
            computer_score += 1
            print('You lose this round!!')
        rounds += 1
        
        play_again = input('Do you want to play again? (yes/no)').lower()
        if play_again != 'yes':
            break
    print(f'Player final score: {player_score}')
    print(f'Computer final score: {computer_score}')
    print(f'Number of rounds played: {rounds}')


        


if __name__ == '__main__':
    play_game()