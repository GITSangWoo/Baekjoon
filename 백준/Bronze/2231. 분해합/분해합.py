N=int(input())

result=0
for i in range(1,N):
  a=list((str(i)))
  x=len(a)
  disum=0
  for j in range(len(a)):
    disum=disum+int(a[j])*(10**(x-1))+int(a[j])
    x=x-1
  if disum==N:
    result=i
    break 
print(result)