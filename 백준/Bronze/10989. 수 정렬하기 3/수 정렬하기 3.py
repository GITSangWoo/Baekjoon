import sys 
N = int(sys.stdin.readline().rstrip()) 

b={}
for line in sys.stdin:
  a=int(line.strip())
  if a in b:
    b[a] += 1
  else:
    b[a] = 1


for i in range(max(b.keys())+1):
  if i not in b:
    continue
  else:
    for _ in range(b[i]):
      print(i)