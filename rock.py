import random
player = None
computer_score = 0
player_score = 0
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    while player not in choices:
        player = input("rock, paper, scissors?:").lower()
    if player == computer:
        print("computer:", computer)
        print("player:", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("computer covers rock so win")
            computer_score += 1
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("player smashes scissors wins")
            player_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("computer smashes scissors so win")
            computer_score += 1
        if computer == "paper":
            print("computer:", computer)
            print("player:", player)
            print("player cuts scissors wins")
            player_score += 1
    elif player == "papers":
        if computer == "scissors":
            print("computer:", computer)
            print("player:", player)
            print("computer cuts rock so win")
            computer_score += 1
        if computer == "rock":
            print("computer:", computer)
            print("player:", player)
            print("player covers scissors wins")
            player_score += 1
    play_again = input("play again? (yes/no):").lower()
    if play_again != "yes":
        print("final scores:")
        print(f"computer:{computer_score}")
        print(f"player:{player_score}")
        break
print("Bye have a nice day")
