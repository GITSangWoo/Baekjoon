
n = int(input())\

a={}
for i in range(n):
  x,y = input().split()
  a[x]=y

result=[k for k,v in a.items() if v == 'enter']
result.sort(reverse=True)
print(*result, sep='\n')