N=int(input())
board = [["*"]*N for i in range(N)]
def star(x,y,N):
  if N==1:
    return

  for i in range(x,x+N):
    for j in range(y,y+N):
      if (i//(N//3))%3==1 and (j//(N//3))%3==1:
        board[i][j]=" "
  
  for i in range(3):
    for j in range(3):
      if i ==1 and j==1:
        continue
      star(x+(i*(N//3)),y+(j*(N//3)),N//3)      

star(0,0,N)
for i in board:
  print(''.join(i))