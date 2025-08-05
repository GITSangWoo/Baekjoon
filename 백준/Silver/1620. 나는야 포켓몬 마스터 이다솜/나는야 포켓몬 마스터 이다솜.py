#1620
N,M=map(int,input().split())
pmd={}
invertpmd={}
for i in range(N):
  name=input()
  pmd[i+1] = name
  invertpmd[name]=i+1
for _ in range(M):
  search=input()
  if search.isdigit():
    print(pmd[int(search)])
  else:
    print(invertpmd[search])