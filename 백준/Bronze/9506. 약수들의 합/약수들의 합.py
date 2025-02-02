# 9506
# N = -1 일때 까지 반복 
N=5
while N != -1:
   # 숫자 입력받기 
  N=int(input())
  if N == -1:
    continue
  # 약수구하기
  comdivlist=[]
  for i in range(1,N+1):
    if N%i == 0:
      comdivlist.append(i)
  comdivlist.remove(N)
  if sum(comdivlist) == N:
    printlist= ''.join(map(lambda x: f" + {x}",comdivlist[1:]))
    print(f"{N} = {comdivlist[0]}{printlist}")
  else: 
    print(f"{N} is NOT perfect.") 