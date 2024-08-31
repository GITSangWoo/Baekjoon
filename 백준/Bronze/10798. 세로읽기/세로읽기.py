A=[list(input()) for i in range(5)]
B=max([len(x) for x in A])
for i in range(B):
  for j in range(5):
    if A[j]==[]:
      pass
    else:
      print(A[j][0],end="")
      A[j].pop(0)