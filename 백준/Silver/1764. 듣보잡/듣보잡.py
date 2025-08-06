N,M = map(int,input().split())
dic={}
for _ in range(N+M):
  val=input()
  dic[val]=dic.get(val,0)+1
result = sorted([k for k,v in dic.items() if v==2])
print(len(result))
print(*result,sep="\n")