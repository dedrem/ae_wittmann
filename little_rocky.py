import random
dict_outcomes = {"rock": {"rock": "it is a draw", "paper": "you win", "scissors": "you lose"},
                 "paper": {"rock": "you lose", "paper": "it is a draw", "scissors": "you win"},
                 "scissors": {"rock": "you win", "paper": "you lose", "scissors": "it is a draw"}}
signs = ["rock", "paper", "scissors"]
while True:
    player_input = input("Rock/Paper/Scissors? ").lower()
    pc_input = signs[random.randint(0, 2)]
    print(f"You chose {player_input}, pc chose {pc_input}, therefore {dict_outcomes[pc_input][player_input]}")
