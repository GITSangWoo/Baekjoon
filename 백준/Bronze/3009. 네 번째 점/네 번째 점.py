X=[]
Y=[]
for i in range(3):
  A,B=list(map(int,input().split()))
  X.append(A)
  Y.append(B)
if X.count(list(set(X))[0]) < X.count(list(set(X))[1]):
  RX=list(set(X))[0]
else: 
  RX=list(set(X))[1]

if Y.count(list(set(Y))[0]) < Y.count(list(set(Y))[1]):
  RY=list(set(Y))[0]
else: 
  RY=list(set(Y))[1]
print(f"{RX} {RY}")