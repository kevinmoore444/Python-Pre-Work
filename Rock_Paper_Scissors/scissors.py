# Player Names Input
player_1_name = input('Player1 - Enter your name: ')
player_2_name = input('Player2 - Enter your name: ')

# Player 1 pick
player_1_pick = input('Player1 - Pick Rock, Paper, or Scissors: ').lower().strip()
while player_1_pick not in ['rock', 'paper', 'scissors']:
    print('Please select a valid choice')
    player_1_pick = input('Player1 - Pick Rock, Paper, or Scissors: ').lower().strip()

# Player 2 pick
player_2_pick = input('Player2 - Pick Rock, Paper, or Scissors: ').lower().strip()
while player_2_pick not in ['rock', 'paper', 'scissors']:
    print('Please select a valid choice')
    player_2_pick = input('Player2 - Pick Rock, Paper, or Scissors: ').lower().strip()

print(f"{player_1_name} picked {player_1_pick} and {player_2_name} picked {player_2_pick}")


# Display Results
match player_1_pick:
    case 'rock':
        if player_2_pick == 'rock':
            print("tie")
        elif player_2_pick == 'paper':
            print(f"{player_2_name} wins")
        elif player_2_pick == 'scissors':
            print(f"{player_1_name} wins")          
    case 'paper':
        if player_2_pick == 'rock':
            print(f"{player_1_name} wins")  
        elif player_2_pick == 'paper':
            print("tie")
        elif player_2_pick == 'scissors':
            print(f"{player_2_name} wins")          
    case 'scissors':
        if player_2_pick == 'rock':
            print(f"{player_2_name} wins")  
        elif player_2_pick == 'paper':
            print(f"{player_1_name} wins") 
        elif player_2_pick == 'scissors':
            print("tie")   





