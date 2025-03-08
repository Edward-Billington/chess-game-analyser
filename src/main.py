import sys
import time
import chess
import chess.pgn
import chess.engine

STOCKFISH_PATH = "/usr/games/stockfish"

def analyze_game_by_color(game, color):
    board = game.board()
    node = game

    while not node.is_end():
        next_node = node.variation(0)
        move = next_node.move

        if board.turn == color:
            info_before = engine.analyse(board, limit=chess.engine.Limit(depth=20))
            eval_before = info_before["score"].pov(color)

            san_move = board.san(move)
            board.push(move)

            info_after = engine.analyse(board, limit=chess.engine.Limit(depth=20))
            eval_after = info_after["score"].pov(color)

            prefix = f"{board.fullmove_number}. " if color == chess.WHITE else f"{board.fullmove_number}... "
            print(f"{prefix}. {san_move} => {eval_before} -> {eval_after}")
        else:
            board.push(move)

        node = node.variation(0)

def process_pgn_stream(pgn_stream):
    game = chess.pgn.read_game(pgn_stream)
    
    if game is None:
        print("No valid game found.")
        sys.exit(1)

    print(game)

    analyze_game_by_color(game, chess.WHITE)
    engine.quit()
    sys.exit(0)

if __name__ == "__main__":
    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
    engine.configure({"Threads": 2})

    process_pgn_stream(sys.stdin)