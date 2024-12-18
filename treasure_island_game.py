print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go?\n Type 'left' or 'right'.\n").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake.\n Type 'wait' to wait for a boat. Type 'swim' to swim cross.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. \n One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("You Loose!")
        elif choice3 == "blue":
            print("You Loose!")
    else:
        print("You Loose!")
else:
    print("You Loose!")
