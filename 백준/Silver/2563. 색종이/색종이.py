A=[[0 for i in range(100)] for j in range(100)]
result=0

for i in range(int(input())):
  x,y=map(int,input().split())
  for j in range(y-1,y+9):
    for k in range(x-1,x+9):
      if A[j][k] == 0:
        A[j][k] = 1
      elif A[j][k] == 1:
        pass 

for i in range(len(A)):
    result+=A[i].count(1)

print(result)