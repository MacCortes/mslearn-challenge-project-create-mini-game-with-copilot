import random

def game_rock_paper_scissors():
    print("Rock, Paper, Scissors, Shoot!")
    #print("-------------------")

    # PROMPT USER FOR INPUT
    user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ").lower()
    # if invalid entry, tell user and try again, valid options: rock, paper, scissors, in upper or lower case
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Oops, invalid entry. Please try again.")
        user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ").lower()

    print("USER CHOICE: ", user_choice)

    # COMPUTER CHOICE (AT RANDOM)
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)
    print("COMPUTER CHOICE: ", computer_choice)

    # DETERMINE THE WINNER
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    # same selection is a tie

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose! Paper beats rock!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose! Scissors beats paper!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lose! Rock beats scissors!")
    else:
        print("Oops, please choose a valid option and try again")

    print("Thanks for playing. Please play again!")
    print("-------------------")

    # option to play again
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again == "yes":
        game_rock_paper_scissors()
    else:
        print("Thanks for playing. Please play again!")
        print("-------------------")

if __name__ == "__main__":
    game_rock_paper_scissors()