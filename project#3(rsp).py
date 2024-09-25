import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock/rpaper/scissors or Q to quit:\n ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("U won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("U won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("U won!")
        user_wins += 1

    else:
        print("U lost!")
        computer_wins += 1

print("U won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")