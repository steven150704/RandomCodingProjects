#Rock Paper Scissors
import random
while True:
    user_input = input('Choose Rock, Paper, or Scissors').capitalize()

    choices = ['Rock', 'Paper', 'Scissors']
    computer_input = random.choice(choices)

    if user_input == computer_input:
        print(f"Both choose {user_input}. Therefore, it is a tie")
    elif user_input == 'Rock':
        if computer_input == 'Paper':
            print(f"Paper beats rock! I win")
        else:
            print(f"You got me this time")
    elif user_input == "Paper":
        if computer_input == "Rock":
            print(f"You chose Paper. Computer chose Rock. You win!")
        else:
            print(f"You chose Paper. Computer chose Scissors. You lose!")
    elif user_input == "Scissors":
        if computer_input == "Paper":
            print(f"You chose Scissors. Computer chose Paper. You win!")
        else:
            print(f"You chose Scissors. Computer chose Rock. You lose!")
    else:
        print("Invalid input. Please choose Rock, Paper, or Scissors.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break