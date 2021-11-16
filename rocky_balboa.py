import random
from string_files import *

game_ended: bool = False
game_loss: bool = False
program_exited: bool = False

score_player: int = 0
score_pc: int = 0


# returns random integer between lowe_bounds and upper_bounds, both inclusive
def get_random_int(lower_bounds: int, upper_bounds: int) -> int:
    return random.randint(lower_bounds, upper_bounds)


# gets player input and transforms it to int
def get_player_guess() -> int:
    player_guess = input(string_prompt_player_guess).lower()
    if player_guess == "schere":
        return 1
    elif player_guess == "stein":
        return 2
    elif player_guess == "papier":
        return 3
    return 0


# ends game and displays result, checks for additional game
def end_game() -> None:
    global program_exited, score_pc, score_player, game_loss, game_ended

    if game_loss:
        print(string_loss)
    else:
        print(string_win)

    if input(string_prompt_continue).lower() != "y":
        program_exited = True
    else:
        score_player = 0
        score_pc = 0
        game_loss = False
        game_ended = False
    return


# updates all game-related values
def update(pc_guess: int, player_guess: int) -> None:
    global score_pc, score_player, game_ended, game_loss

    print(f"Du hast {signs[player_guess-1]}, PC hat {signs[pc_guess-1]}")

    if pc_guess == player_guess:
        return
    elif pc_guess == SCHERE:
        if player_guess == STEIN:
            score_player += 1
        if player_guess == PAPIER:
            score_pc += 1
    elif pc_guess == STEIN:
        if player_guess == SCHERE:
            score_pc += 1
        if player_guess == PAPIER:
            score_player += 1
    else: # PAPIER
        if player_guess == STEIN:
            score_pc += 1
        elif player_guess == SCHERE:
            score_player += 1

    if score_player == 3:
        game_ended = True
    elif score_pc == 3:
        game_ended = True
        game_loss = True

    return


# prints current score
def print_scores() -> None:
    global score_pc, score_player
    print(f"Du hast {score_player} Punkte, der PC hat {score_pc} Punkte!\n\n")
    return


def main():
    print(string_welcome)
    while not program_exited:
        while not game_ended:
            current_pc_guess = get_random_int(1, 3)
            current_player_guess = get_player_guess()
            update(current_pc_guess, current_player_guess)
            print_scores()
        end_game()


if __name__ == "__main__":
    main()



