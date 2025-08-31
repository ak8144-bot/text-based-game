import random


def display_instructions():

    print('=' * 50)

    print('WELCOME TO ROCK, PAPER, SCISSORS GAME!')

    print('=' * 50)

    print('Game Rules:')

    print('- Rock beats Scissors')

    print('- Scissors beats Paper')

    print('- Paper beats Rock')

    print('- Same choices result in a tie')

    print('\nHow to play:')

    print("- Enter 'rock', 'paper', or 'scissors' when prompted")

    print("- Enter 'quit' or 'exit' to stop playing")

    print("- Type 'mode' during the game to switch modes")

    print('\nModes:')

    print('- Normal: Fair game, random computer choices')

    print('- Unbeatable: Computer always wins')

    print('=' * 50)


def choose_mode():

    while True:

        choice = input('Choose mode - normal/unbeatable: ').lower().strip()

        if choice in ['normal', 'n']:

            return 'normal'

        if choice in ['unbeatable', 'u']:

            return 'unbeatable'

        print("Please type 'normal' or 'unbeatable'.")


def get_computer_choice(mode, player_choice=None):

    choices = ['rock', 'paper', 'scissors']

    if mode == 'normal' or player_choice is None:

        return random.choice(choices)

    counters = {

        'rock': 'paper',

        'paper': 'scissors',

        'scissors': 'rock'

    }

    return counters.get(player_choice, random.choice(choices))


def get_player_choice():

    while True:

        choice = input("\nEnter your choice (rock/paper/scissors), 'mode' to switch, or 'quit' to exit: ").lower().strip()

        if choice in ['quit', 'exit', 'q']:

            return 'quit'

        if choice in ['mode', 'm']:

            return 'mode'

        if choice in ['rock', 'paper', 'scissors']:

            return choice

        print("Invalid choice! Use 'rock', 'paper', 'scissors', 'mode', or 'quit'.")


def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:

        return 'tie'

    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'scissors' and computer_choice == 'paper') or \
       (player_choice == 'paper' and computer_choice == 'rock'):

        return 'player'

    return 'computer'


def display_round_result(player_choice, computer_choice, winner):

    print(f"\nYou chose: {player_choice.capitalize()}")

    print(f"Computer chose: {computer_choice.capitalize()}")

    print('-' * 30)

    if winner == 'tie':

        print("It's a TIE!")

    elif winner == 'player':

        print('You WIN this round!')

    else:

        print('Computer WINS this round!')


def display_score(player_wins, computer_wins, ties, mode):

    total_games = player_wins + computer_wins + ties

    print('\n' + '=' * 40)

    print(f'MODE: {mode.upper()}')

    print('CURRENT SCORE:')

    print(f'Your wins: {player_wins}')

    print(f'Computer wins: {computer_wins}')

    print(f'Ties: {ties}')

    print(f'Total games played: {total_games}')

    print('=' * 40)


def display_final_stats(player_wins, computer_wins, ties):

    total_games = player_wins + computer_wins + ties

    print('\n' + '=' * 50)

    print('FINAL GAME STATISTICS:')

    print('=' * 50)

    print(f'Total games played: {total_games}')

    print(f'Your wins: {player_wins}')

    print(f'Computer wins: {computer_wins}')

    print(f'Ties: {ties}')

    if total_games > 0:

        win_percentage = (player_wins / total_games) * 100

        print(f'Your win percentage: {win_percentage:.1f}%')

        if player_wins > computer_wins:

            print('Congratulations! You won overall!')

        elif computer_wins > player_wins:

            print('Computer won overall! Better luck next time!')

        else:

            print("It's an overall tie! Great game!")

    print('Thanks for playing!')

    print('=' * 50)


def play_game():

    player_wins = 0

    computer_wins = 0

    ties = 0

    display_instructions()

    mode = choose_mode()

    while True:

        player_choice = get_player_choice()

        if player_choice == 'quit':

            break

        if player_choice == 'mode':

            print('\nSwitching mode...')

            mode = choose_mode()

            continue

        if mode == 'unbeatable':

            computer_choice = get_computer_choice(mode, player_choice)

        else:

            computer_choice = get_computer_choice(mode)

        winner = determine_winner(player_choice, computer_choice)

        display_round_result(player_choice, computer_choice, winner)

        if winner == 'player':

            player_wins += 1

        elif winner == 'computer':

            computer_wins += 1

        else:

            ties += 1

        display_score(player_wins, computer_wins, ties, mode)

        while True:

            cont = input('\nPlay another round? (y/n): ').lower().strip()

            if cont in ['y', 'yes', 'n', 'no']:

                break

            print("Please enter 'y' or 'n'.")

        if cont in ['n', 'no']:

            break

    display_final_stats(player_wins, computer_wins, ties)


if __name__ == '__main__':

    play_game()