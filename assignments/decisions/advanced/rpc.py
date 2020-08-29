p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

if p1_move == p2_move:
    print("It's a draw")
else:
    if p1_move == "rock":
        if p2_move == "paper":
            winner = "Player 2"
        else:
            winner = "Player 1"
    elif p1_move == "paper":
        if p2_move == "scissors":
            winner = "Player 2"
        else:
            winner = "Player 1"
    elif p1_move == "scissors":
        if p2_move == "rock":
            winner = "Player 2"
        else:
            winner = "Player 1"
    print("Winner:", winner)