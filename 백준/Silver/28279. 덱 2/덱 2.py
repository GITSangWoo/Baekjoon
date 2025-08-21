import sys 
from collections import deque

N = int(sys.stdin.readline())
x=deque([])
for _ in range(N):
  cmd = list(map(int,sys.stdin.readline().split()))
  if len(cmd)>1:
    if cmd[0] == 1:
      x.appendleft(cmd[1])
    elif cmd[0] ==2:
      x.append(cmd[1])
  else:
    if cmd[0] == 3:
      if len(x)>0:
        print(x.popleft())
      else:
        print(-1)
    elif cmd[0] == 4:
      if len(x)>0:
        print(x.pop())
      else:
        print(-1)
    elif cmd[0] == 5:
      print(len(x))
    elif cmd[0] == 6:
      if len((x))>0:
        print(0)
      else :
        print(1)
    elif cmd[0] == 7:
      if len(x)>0:
        print(x[0])
      else:
        print(-1)
    elif cmd[0] == 8:
      if len(x)>0:
        print(x[-1])
      else:
        print(-1)  