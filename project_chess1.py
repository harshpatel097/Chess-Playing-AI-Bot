#!/usr/bin/env python
# coding: utf-8

# In[70]:


import keras 
from keras.models import load_model

import numpy as np

opt = keras.optimizers.Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0)
model = load_model('trained_model_final_bs32_225_dg.h5')

model.compile(loss='binary_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])


# In[71]:


model.summary()


# In[72]:


#import sys
import matplotlib.pyplot as plt
from PIL import Image
import h5py
#sys.modules['Image'] = Image 

#index = np.random.randint(63)
#from keras.preprocessing import image

l = [None] * 64

for r in range(1,65):
  img = Image.open('New1/opencv_frame1_'+str(r)+'.jpg')
  img = np.array(img)
  img = np.reshape(img,(100,100,3))
  #y = image.img_to_array(img)

  #print(y.shape)
  print(img.shape)

  plt.imshow(img)
  plt.show()
  img = np.reshape(img,(1,100,100,3))
  print(img.shape)

  y = model.predict_classes(img)
  print(y)

  if y==0:
    classes='E'
  elif y==1:
    classes='B'
  elif y==2:
    classes='K'
  elif y==3:
    classes='N'
  elif y==4:
    classes='P'
  elif y==5:
    classes='Q'
  elif y==6:
    classes='R'
  elif y==7:
    classes='b'
  elif y==8:
    classes='k'
  elif y==9:
    classes='n'
  elif y==10:
    classes='p'
  elif y==11:
    classes='q'
  else:
    classes='r'


  print(classes)
  
  l[r-1]=classes


# In[73]:


from array import *

m = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
     ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]


# In[74]:


s=0
for i in range(8) :
    for j in range(8):
        m[i][j] = l[s]
        s +=1

print(m)


# In[75]:


import chess
fen=""
count1=0
count2=0
for r in m:
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


# In[79]:


import chess
import chess.uci

#Let's try our code with the starting position of chess:
#fen = 'rnbqkb1r/pp1ppp1p/5np1/2p5/2P1P3/3B4/PP1P1PPP/RNBQK1NR w - - 0 0'
#board = chess.Board(fen)
handler = chess.uci.InfoHandler()
#print(board)
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


# In[ ]:




