import chess
import chess.uci

#Let's try our code with the starting position of chess:
fen = 'rnbqkb1r/pp1ppp1p/5np1/2p5/2P1P3/3B4/PP1P1PPP/RNBQK1NR w - - 0 0'
board = chess.Board(fen)
handler = chess.uci.InfoHandler()
print(board)
#Now make sure you give the correct location for your stockfish engine file
#...in the line that follows: e.g., /home/.../stockfish_6_x64
engine = chess.uci.popen_engine('stockfish\Windows\stockfish_10_x64')

engine.info_handlers.append(handler)
engine.position(board)
if board.turn: print ('White to move')
else: print ('black to move')
m = -100
bestmove = ''
for el in board.legal_moves:
    engine.go(searchmoves=[el],movetime=500)
    #print (str(el), 'eval = ', round(handler.info["score"][1].cp/100.0,2))
    if round(handler.info["score"][1].cp/100.0,2) > m :
        m = round(handler.info["score"][1].cp/100.0,2)
        bestmove = el
        
board.push(bestmove)
print(board)
print('\n the bestmove is : ',str(bestmove),'eval = ' ,  m)
