N,M=map(int,input().split())
A=[]
B=[]
for j in range(N): 
  A += list(map(int,input().split())) 
for j in range(N):
  B += list(map(int,input().split()))

summed_list=[a+b for a,b in zip(A,B)]

for i in range(0,len(summed_list),N):
  print(*summed_list[i:i+N])