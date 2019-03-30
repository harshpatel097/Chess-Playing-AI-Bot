import chess
import numpy as np
from array import *
a=[['r','n','b','q','k','b','n','r'],['p','p','p','p','p','p','p','p'],['E','E','E','E','E','E','E','E'],['E','E','E','E','E','E','E','E'],['E','E','E','E','E','E','E','E'],['E','E','P','E','E','E','E','E'],['P','P','E','P','P','P','P','P'],['R','N','B','Q','K','B','N','R']]
fen=""
count1=0
count2=0
for r in a:
    s=""
    count1=count1+1;
    count2=0;
    for c in r:
        if c=='E':
            count2=count2+1;
        else:
            if count2!=0:
                s=s+str(count2);
            s=s+c;
            count2=0;
    if count2!=0:
        s=s+str(count2);
    if count1!=1:
        fen=fen+'/'+s
    else:
        fen=fen+s
fen=fen+' b - - 0 0'
print(fen)
board=chess.Board(fen)
print(board)


