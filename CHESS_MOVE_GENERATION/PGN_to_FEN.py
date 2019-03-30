import chess
import chess.pgn
pgn=open("Adams.pgn")
first_game=chess.pgn.read_game(pgn)
board=first_game.board()
for move in first_game.mainline_moves():
    board.push(move)
fen=board.fen()
print(board)
print(fen)
