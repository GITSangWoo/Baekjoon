T = int(input())
Boolean_list=[True]*1000000
Boolean_list[0:2]=[False,False]

for i in range(len(Boolean_list)):
  if Boolean_list[i]:
    for j in range(i*i,len(Boolean_list),i):
      Boolean_list[j]=False
 
prime_list=[i for i, val in enumerate(Boolean_list) if val]

for _ in range(T):
  N=int(input())
  cnt=0
  for i in prime_list:
    if i > N//2:
      break
    if Boolean_list[N-i]:
      cnt+=1
  print(cnt)