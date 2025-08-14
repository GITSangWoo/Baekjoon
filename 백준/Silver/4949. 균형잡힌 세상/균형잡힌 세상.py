while True:
  a= list(input())

  stackA=[]
  if a[0] == '.':
    break

  for i in a:
    if i == '(' or i == ')' or i == '[' or i == ']':
      stackA.append(i)
      if len(stackA) >1:
        if stackA[-1] == ')' and  stackA[-2]=='(':
          stackA.pop(-1)
          stackA.pop(-1)
        elif stackA[-1] == ']' and  stackA[-2]=='[':
          stackA.pop(-1)
          stackA.pop(-1)        
  if len(stackA) == 0 :
    print('yes')
  else:
    print('no')