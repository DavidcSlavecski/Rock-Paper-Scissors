import random
import operator

#function get_player_choice choice object
def get_player_choice():
    true
# Function to get the player's choice object
def get_player_choice():
    choice = input("Choose Rock, Paper or Scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper or Scissors.")
        choice = input("Choose Rock, Paper or Scissors: ").lower()
    return choice

# Function for obtaining computer selection
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function for determining the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# The main function of the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Launching the game
if __name__ == "__main__":
    play_game()
