N,M=map(int,input().split())
x=list(range(1,N+1))
for m in range(M):
  I,J=map(int,input().split())
  for k in range(J,I,-1):
    for z in range(I,J):
      tmp=x[z-1]
      x[z-1]=x[z]
      x[z]=tmp
    J=J-1
print(*x)