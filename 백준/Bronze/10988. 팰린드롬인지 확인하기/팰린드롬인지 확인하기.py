a=list(input())
b=1
for i in range(int(len(a)/2)):
  if a[i] ==a[len(a)-i-1]:
    b=1
  else:
    b=0
    break;
print(b)