# N 과 K 입력받기
N, K = map(int,input().split())
# N의 약수들 중 K 번째로 작은 수를 출력하는 프로그램 만들기 
comdivlist=[]
for i in range(1,N+1):
  if N%i == 0:
    comdivlist.append(i)

result=comdivlist

if len(result) < K:
  print(0)
else:  
  print(result[K-1])  