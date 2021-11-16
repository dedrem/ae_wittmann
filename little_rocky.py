import random
dict = {"rock": {"rock": "draw", "paper": "you win", "scissors": "you lose"},
        "paper": {"rock": "you lose", "paper": "draw", "scissors": "you win"},
        "scissors": {"rock": "you win", "paper": "you lose", "scissors": "draw"}}
signs = ["rock", "paper", "scissors"]
while True:
    player_input = input("Rock/Paper/Scissors? ").lower()
    pc_input = signs[random.randint(0, 2)]
    print(f"You chose {player_input}, pc chose {pc_input}, therefore {dict[pc_input][player_input]}")


