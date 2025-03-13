a1,a0 = map(int,input().split())
c=int(input())
n0=int(input())

result=0
for i in range(n0,101):
  if a0 <= (c-a1)*i:
    result=1
  else:
    result=0
    break
print(result)