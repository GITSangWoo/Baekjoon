T = int(input())
for _ in range(T):
  A,B=map(int,input().split())
  mul = A*B
  if A>=B:
    C=None
    while C != 0:
      C= A%B
      A = B
      B = C
      gcd = A

  if B>=A:
    C=None
    while C != 0:
      C= B%A
      B = A
      A = C
      gcd = B

  lcm = int(mul/gcd)
  print(lcm)