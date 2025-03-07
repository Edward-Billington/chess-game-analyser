import sys
import time
import chess.pgn

pgn_stream = sys.stdin

while True:
    game = chess.pgn.read_game(pgn_stream)
    if game is None:
        break

    board = game.end().board()
    print(game.headers)
    print(board)
    print("Game finished with result:", game.headers.get("Result"))
    print(game)
    print("-" * 40)

    time.sleep(10)


