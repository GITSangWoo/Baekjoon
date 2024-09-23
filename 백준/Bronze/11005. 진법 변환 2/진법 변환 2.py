N,B = map(int,input().split())
total=0
result=0
answer=[]
for i in range(30,-1,-1):
  result = int(N/B**i)
  if result==0:
    if len(answer)==0 or answer[0]=='0': 
      continue
    else :
      answer.append(str(result))
      N=N%B**i 
      continue
  elif result >=10 : 
    answer.append(chr(result+55))
    N=N%B**i 
    continue
  else:
    answer.append(str(result))
    N=N%B**i 
    continue

print(''.join(answer))