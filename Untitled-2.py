def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors', 'quit']
    while True:
        user_choice = input('Enter your choice (rock, paper, scissors, or quit): ').lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print('Invalid choice. Please try again.')

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 'tie'
    elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
         (player1_choice == 'scissors' and player2_choice == 'paper') or \
         (player1_choice == 'paper' and player2_choice == 'rock'):
        return 'player1'
    else:
        return 'player2'

def main():
    while True:
        player1_choice = get_user_choice()
        if player1_choice == 'quit':
            break
        player2_choice = get_user_choice()
        if player2_choice == 'quit':
            break
        winner = determine_winner(player1_choice, player2_choice)
        if winner == 'tie':
            print('It\'s a tie!')
        elif winner == 'player1':
            print(f'Player 1 wins! {player1_choice} beats {player2_choice}.')
        else:
            print(f'Player 2 wins! {player2_choice} beats {player1_choice}.')

if __name__ == '__main__':
    main()