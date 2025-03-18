N,M=map(int,input().split()) # N=세로 M=가로

# 8*8 체스판의 배열 기준 홀수열 짝수열  
a=["B","W","B","W","B","W","B","W"]
b=["W","B","W","B","W","B","W","B"]
e=[]
f=[]
h=[]
# N번째줄 순회 
for i in range(N):
  c=[]
  c=input()
  # 짝수 (0,2)열을 a로 비교할때 바꿔야하는 개수 
  d=[]
  if i % 2 == 0:
    for j in range(M-7):
      e=c[j:8+j]
      d.append(sum(1 for z,x in zip(a,e) if z!=x))
    f.append(list(d))
  if i % 2 == 1:
    for j in range(M-7):
      e=c[j:8+j]
      d.append((sum(1 for z,x in zip(b,e) if z!=x)))
    f.append(list(d))
  # 홀수 (1,3)열을 a로 비교할때 바꿔야하는 개수 
  g=[]
  if i % 2 == 0:
    for j in range(M-7):
      e=c[j:8+j]
      g.append(sum(1 for z,x in zip(b,e) if z!=x))
    h.append(list(g))
  if i % 2 == 1:
    for j in range(M-7):
      e=c[j:8+j]
      g.append(sum(1 for z,x in zip(a,e) if z!=x))
    h.append(list(g))



# 연속된 칸과줄의 8*8의 조합으로 가장작은 합이 나오는 경우 구하기 

result=[]
for i in range(N-7):
 for j in range(M-7):
    cnt=[]
    for k in range(i,8+i):
      cnt.append(f[k][j])
    result.append(sum(cnt))
    cnt=[]
    for k in range(i,8+i):
      cnt.append(h[k][j])
    result.append(sum(cnt))

print(min(result))
