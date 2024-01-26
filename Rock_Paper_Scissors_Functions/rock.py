

def display_opening_message():
    print("Let's play Rock Paper Scissors")

def read_required_string(prompt):
    value = input(f"{prompt} ").strip()
    while value == "":
        print("Must provide a value")
        value = input(f"{prompt} ").strip()
    return value

def request_name(player):
    player_name = read_required_string(f"{player} - Enter your name: ")
    return player_name

def request_pick(player_name):
    player_pick = input(f'{player_name} - Pick Rock, Paper, or Scissors: ').lower().strip()
    while player_pick not in ['rock', 'paper', 'scissors']:
        print('Please select a valid choice')
        player_pick = input('Player2 - Pick Rock, Paper, or Scissors: ').lower().strip()
    return player_pick

def play_game(player_1_name, player_1_pick, player_2_name, player_2_pick):
    match player_1_pick:
        case 'rock':
            if player_2_pick == 'rock':
                print("tie")
                return 0
            elif player_2_pick == 'paper':
                print(f"{player_2_name} wins")
                return 2
            elif player_2_pick == 'scissors':
                print(f"{player_1_name} wins")
                return 1       
        case 'paper':
            if player_2_pick == 'rock':
                print(f"{player_1_name} wins")
                return 1
            elif player_2_pick == 'paper':
                print("tie")
                return 0
            elif player_2_pick == 'scissors':
                print(f"{player_2_name} wins")
                return 2      
        case 'scissors':
            if player_2_pick == 'rock':
                print(f"{player_2_name} wins")
                return 2 
            elif player_2_pick == 'paper':
                print(f"{player_1_name} wins") 
                return 1
            elif player_2_pick == 'scissors':
                print("tie")
                return 0



def print_score(player_1_score, player_2_score, ties, player_1_name, player_2_name):
    print("Score")
    print("="*20)
    print(f"{player_1_name}: {player_1_score}")
    print(f"{player_2_name}: {player_2_score}")
    print(f"Ties :{ties}")
    print("="*20)

# Collect names and run game
def setup_game():
    player_1_name = request_name("player_1")
    player_2_name = request_name("player_2")
    run_game(player_1_name, player_2_name)

# Run game logic
def run_game(player_1_name, player_2_name, player_1_score=0, player_2_score=0, ties=0):

    # Display opening message
    display_opening_message()
    # Each player picks rock, paper or scissors
    player_1_pick = request_pick(player_1_name)
    player_2_pick = request_pick(player_2_name)
    # Determine who wins
    result = play_game(player_1_name, player_1_pick, player_2_name, player_2_pick)
    # Track/Display score 
    if result == 1:
        player_1_score+=1
    elif result == 2:
        player_2_score+=1
    else:
        ties+=1
    # Print Score
    print_score(player_1_score, player_2_score, ties, player_1_name, player_2_name)
    # Ask to play again
    play_again = input('Play again? [y/n]: ').lower().strip()
    if play_again == 'y':
        run_game(player_1_name, player_2_name, player_1_score, player_2_score, ties)
    elif play_again == 'n':
        return
    else:
        print('Please select a valid response')





setup_game()
