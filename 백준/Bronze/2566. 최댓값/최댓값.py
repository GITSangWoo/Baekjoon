A=[]
for j in range(1,10):
  A += list(map(int,input().split()))  
print(max(A))
L= A.index(max(A))//9 + 1
L2 = A.index(max(A))%9 + 1
print(L,L2) 