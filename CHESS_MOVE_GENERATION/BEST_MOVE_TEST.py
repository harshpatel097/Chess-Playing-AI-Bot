import chess
import chess.uci

#Let's try our code with the starting position of chess:
file = open(r"fen.txt","r")
fen = file.readline()
#'rnbqkbnr/ppp1pppp/8/3P4/8/8/PPPP1PPP/RNBQKBNR b - - 0 0'
file.close()
board = chess.Board(fen)
print(board)
handler = chess.uci.InfoHandler()
#Now make sure you give the correct location for your stockfish engine file
#...in the line that follows: e.g., /home/.../stockfish_6_x64
engine = chess.uci.popen_engine('/home/pi/Stockfish/src/stockfish')
engine.info_handlers.append(handler)
engine.position(board)
if board.turn: print ('White to move')
else: print ('black to move')

m = -100
bestmove = ''
print(board.legal_moves.count())
for el in board.legal_moves:
    engine.go(searchmoves=[el],movetime=500)
    #print (str(el), 'eval = ', round(handler.info["score"][1].cp/100.0,2))
    if round(handler.info["score"][1].cp/100.0,2) > m :
        m = round(handler.info["score"][1].cp/100.0,2)
        bestmove = el
        
board.push(bestmove)
print(board)
print('\n the bestmove is : ',str(bestmove),'eval = ' ,  m)
