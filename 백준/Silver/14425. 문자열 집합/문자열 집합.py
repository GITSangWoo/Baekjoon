N,M = map(int,input().split())
a=set([input()for i in range(N)])

b=[input()for i in range(M)]

result = 0
for i in b:
  if i in a:
    result+=1
print(result)
