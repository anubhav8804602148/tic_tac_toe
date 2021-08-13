from os import system, name
from numpy import random as rnd 
import time
def show(p, msg):
  if name=='nt':
    _ = system('cls')
  else:
    _ = system('clear')
  screen='''
                ||                ||
          {}    ||      {}        ||    {} 
               0||               1||          2
      ==========================================
                ||                ||
          {}    ||      {}        ||    {}  
               3||               4||          5
      ==========================================
                ||                ||
          {}    ||      {}        ||    {}  
               6||               7||          8

                {}
  '''.format(p[0],p[1],p[2],
            p[3],p[4],p[5],
            p[6],p[7],p[8], msg)
  
  print(screen)
curr_pos = ["  ","  ","  ","  ","  ","  ","  ","  ","  ",]
show(curr_pos,"")
def p1win():
  print('''

          Player 1 Wins! Good Job. 
  
  ''')
  exit()
def p2win():
  print('''

          Player 2 Wins! Good Job. 
  
  ''')
  exit()
def get_out():
  
  print('''

          You chose not to move!! Good Bye. 
  
  ''')
  exit()
def get_computer_move(curr_pos):
  
  av_move = [0,1,2,3,4,5,6,7,8]
  line = str(curr_pos[0]+curr_pos[1]+curr_pos[2]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [0,1,2]
  line = str(curr_pos[3]+curr_pos[4]+curr_pos[5]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [3,4,5]
  line = str(curr_pos[6]+curr_pos[7]+curr_pos[8]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [6,7,8]
  line = str(curr_pos[0]+curr_pos[3]+curr_pos[6]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [0,3,6]
  line = str(curr_pos[1]+curr_pos[4]+curr_pos[7]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [1,4,7]
  line = str(curr_pos[2]+curr_pos[5]+curr_pos[8]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [2,5,8]
  line = str(curr_pos[0]+curr_pos[4]+curr_pos[8]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [0,4,8]
  line = str(curr_pos[2]+curr_pos[4]+curr_pos[6]).replace(" ","").replace("O","")
  if len(line)==2:
    av_move = [2,4,6]
  
  for e in av_move:
    if curr_pos[e] != "  ":
      av_move.remove(e)
  return rnd.choice(av_move)
def won(curr_pos):
  if curr_pos[0]==curr_pos[1] and curr_pos[1]==curr_pos[2] and curr_pos[0]!="  ":
    if curr_pos[0]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[3]==curr_pos[4] and curr_pos[4]==curr_pos[5] and curr_pos[3]!="  ":
    if curr_pos[3]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[6]==curr_pos[7] and curr_pos[7]==curr_pos[8] and curr_pos[6]!="  ":
    if curr_pos[6]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[0]==curr_pos[3] and curr_pos[3]==curr_pos[6] and curr_pos[0]!="  ":
    if curr_pos[0]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[1]==curr_pos[4] and curr_pos[4]==curr_pos[7] and curr_pos[1]!="  ":
    if curr_pos[1]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[2]==curr_pos[5] and curr_pos[5]==curr_pos[8] and curr_pos[2]!="  ":
    if curr_pos[2]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[0]==curr_pos[4] and curr_pos[4]==curr_pos[8] and curr_pos[0]!="  ":
    if curr_pos[0]==" X":
      p1win()
    else:
      p2win()
    return True
  if curr_pos[2]==curr_pos[4] and curr_pos[4]==curr_pos[6] and curr_pos[2]!="  ":
    if curr_pos[2]==" X":
      p1win()
    else:
      p2win()
    return True


all_moves=""
turn = 1
while not won(curr_pos):
  msg = ""
  try:
    move = int(input("Enter Your move : ")) if turn==1 else get_computer_move(curr_pos)
  except:
    get_out()
  all_moves += str(move)
  if curr_pos[move]=="  " and move < 9 and move >= 0:
    curr_pos[int(move)] = " X" if turn==1 else " O"
    turn = 1 - turn
  else:
    msg = "Not a valid move!!"
  time.sleep(3)
  show(curr_pos, all_moves+msg)
