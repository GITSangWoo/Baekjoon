def is_prime(N):
  if N in prime_set:
    return True
  for p in prime_list:
    if p*p > N:
      break
    if N%p==0:
      return False
  return True

n=int(input())
prime_boolean=[True for i in range(63247)]
prime_boolean[0:2]=[False,False]

for i in range(len(prime_boolean)):
  if prime_boolean[i]:
    for j in range(i*i,len(prime_boolean),i):
      prime_boolean[j] = False

prime_list=[i for i,val in enumerate(prime_boolean) if val ]
prime_set= set(prime_list)
for _ in range(n):
  N=int(input())
  if N < 2:
    print(2)
    continue
  if is_prime(N): 
    print(N)
    continue
  else:           
    while True:
      N+=1
      if is_prime(N):
        print(N)
        break