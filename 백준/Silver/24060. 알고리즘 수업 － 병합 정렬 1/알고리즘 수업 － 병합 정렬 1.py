#24060

def merge_sort(A,p,r,K,cnt):
  if p<r:
    q=(p+r)//2
    result = merge_sort(A,p,q,K,cnt)
    if result is not None:
      return result
    result = merge_sort(A,q+1,r,K,cnt)
    if result is not None:
      return result
    result = merge(A,p,q,r,K,cnt)
    if result is not None:
      return result

def merge(A,p,q,r,K,cnt):
  tmp = []
  i = p
  j= q+1
  while (i<=q and j<=r):
    if A[i] <= A[j]:
      tmp.append(A[i]) 
      i+=1
    else:
      tmp.append(A[j])
      j+=1
  while i<=q:
    tmp.append(A[i])
    i+=1
  while j<=r:
    tmp.append(A[j])
    j+=1
  
  for k in range(len(tmp)):
    A[p+k]=tmp[k]
    cnt[0]+=1
    if cnt[0] ==K:
      return tmp[k]

N,K = map(int,input().split())
A = list(map(int,input().split()))
cnt =[0]
result = merge_sort(A,0,len(A)-1,K,cnt)
if result is not None:
  print(result)
else:
  print(-1)