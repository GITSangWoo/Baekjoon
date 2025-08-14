import sys 

def judge(a):
  stackA=[]
  if a[0] == ')'  or len(a) % 2 > 0:
    return False 

  for i in a:
    stackA.append(i)
    if len(stackA) > 1:
      if stackA[-1] == ')' and  stackA[-2]=='(':
        stackA.pop(-1)
        stackA.pop(-1)

  if len(stackA) == 0 :
    return True 
  else :
    return False 
    
      
T = int(sys.stdin.readline())

for _ in range(T):
    a = list(sys.stdin.readline().rstrip()) 
    if judge(a):
        print("YES")
    else:
        print("NO")    