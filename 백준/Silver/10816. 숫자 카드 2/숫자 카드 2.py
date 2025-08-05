N=int(input())
a=list(map(int,input().split()))
dic={}
for x in a:
  dic[x]=dic.get(x,0)+1 
M=int(input())
b=list(map(int,input().split()))
result = []
for i in b:
  val = dic.get(i,0)
  result.append(val)

print(*result)