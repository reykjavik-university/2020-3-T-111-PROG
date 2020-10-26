import random
from typing import Tuple


def main():
    # Ensure that games play out deterministically by specifying the random seed.
    # This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in Mimir.
    random.seed(1337)
    snakes, ladders = read_board_layout_from_input()
    player1, player2 = read_player_names_from_input()
    winner = play_game(snakes, ladders, player1, player2)
    declare_winner(winner)


def read_board_layout_from_input() -> Tuple[list, list]:
    """Asks the user to provide the number and locations of the snakes and ladders on the board.

    Returns two lists, the first with the snakes, the second with the ladders.
    Each element in the lists is a tuple with two numbers: (from, to)"""
    snake_and_ladder_count = int(input("Number of snakes and ladders: "))
    all_position_pairs = [
        read_snake_ladder_position_from_input(number=i + 1)
        for i in range(snake_and_ladder_count)
    ]
    snakes = [
        (from_where, to_where)
        for from_where, to_where in all_position_pairs
        if from_where > to_where
    ]
    ladders = [
        (from_where, to_where)
        for from_where, to_where in all_position_pairs
        if from_where < to_where
    ]
    return snakes, ladders


def read_snake_ladder_position_from_input(number: int) -> Tuple[int, int]:
    """ Reads the numbers of the two squares, which are connected by a snake or ladder, and returns as a tuple """
    from_where_to_where = input(f"Snake/ladder {number} leads from where to where: ")
    from_position, _, to_position = from_where_to_where.partition(" ")
    return (int(from_position), int(to_position))


def read_player_names_from_input() -> Tuple[str, str]:
    """ Reads the player names from standard input and returns as a tuple """
    player1 = input("Name of player 1: ")
    player2 = input("Name of player 2: ")
    return player1, player2


def play_game(snakes: list, ladders: list, player1: str, player2: str) -> str:
    """ Simulates a game of snakes and ladders. Returns the name of the player who won. """
    player_positions = [0, 0]
    player_names = (player1, player2)
    current_player = 0
    while neither_player_has_reached_last_square(player_positions):
        current_player = play_one_turn(
            snakes, ladders, player_positions, player_names, current_player
        )
    winner = player_names[0] if player_positions[0] >= 100 else player_names[1]
    return winner


def neither_player_has_reached_last_square(positions: list) -> bool:
    """ Returns True if neither player has reached the last square, otherwise False """
    return positions[0] < 100 and positions[1] < 100


def play_one_turn(
    snakes: list,
    ladders: list,
    player_positions: list,
    player_names: tuple,
    current_player: int,
) -> int:
    """ Executes the steps performed in a single turn and describes (prints) how the player fared """
    roll = roll_die()
    move_player(player_positions, current_player, roll)
    show_roll_and_new_position(
        roll=roll,
        position=player_positions[current_player],
        player=player_names[current_player],
    )
    adjust_position_if_on_snake(player_positions, player_names, current_player, snakes)
    adjust_position_if_on_ladder(
        player_positions, player_names, current_player, ladders
    )
    return determine_next_player(current_player, roll)


def move_player(player_positions: list, current_player: int, roll: int) -> None:
    """ Advance player according to roll whilst ensuring that player doesn't exceed square 100 """
    player_positions[current_player] = min(player_positions[current_player] + roll, 100)


def determine_next_player(current_player: int, roll: int) -> int:
    """ Alternates the player index between 0 and 1 if die roll was less than 6 """
    other_player = 1 - current_player
    return other_player if roll < 6 else current_player


def roll_die() -> int:
    """ Simulate a roll of a 6-sided die """
    return random.randint(1, 6)


def adjust_position_if_on_snake(
    player_positions: list, player_names: tuple, current_player: int, snakes: list
) -> None:
    """ Checks if the player landed on a snake and adjusts the player's position accordingly if that's the case """
    for from_where, to_where in snakes:
        if player_positions[current_player] == from_where:
            player_positions[current_player] = to_where
            show_snake_message(player_names[current_player], to_where)
            return


def adjust_position_if_on_ladder(
    player_positions: list, player_names: tuple, current_player: int, ladders: list
) -> None:
    """ Checks if the player has a ladder to climb and adjusts the player's position accordingly if that's the case """
    for from_where, to_where in ladders:
        if player_positions[current_player] == from_where:
            player_positions[current_player] = to_where
            show_ladder_message(player_names[current_player], to_where)
            return


def show_roll_and_new_position(roll: int, position: int, player: str) -> None:
    print(f"{player} rolled {roll} and is now at square {position}")


def show_snake_message(player_name: str, destination_square: int) -> None:
    print(
        f"Darn! A bloody snake brought {player_name} down to square {destination_square}"
    )


def show_ladder_message(player_name: str, destination_square: int) -> None:
    print(f"Splendid! {player_name} climbed a ladder up to square {destination_square}")


def declare_winner(winner: str) -> None:
    print(f"{winner} won the game")

main()
