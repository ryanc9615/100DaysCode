import random

outcome = ["rock", "paper", "scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_outcome = outcome[user_input]
print(f"User chose: {user_outcome}")

computer_choice = random.randint(0,2)
computer_outcome = outcome[computer_choice]
print(f"Computer chose: {computer_outcome}")


if user_input < 0 or user_input > 3:
    print("Incorrect selection please try again!")
elif computer_choice == 0 and user_input == 2:
    print("Computer Wins!")
elif user_input == 0 and computer_choice == 2: 
    print("User Wins!")
elif computer_choice > user_input:
    print("Computer Wins!")
elif user_input > computer_choice:
    print("User Wins!")
elif computer_choice == user_input:
    print("It's a draw!")



