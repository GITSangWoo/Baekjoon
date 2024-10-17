while True: 
  a,b = map(int,input().split())
  if a == 0 & b==0:
    break; 
  # 어느 쪽으로 나누었을때 둘 중에 하나라도 나머지가 없으면 배수또는 약수
  if a%b==0 or b%a==0:
    if a%b == 0: 
      print("multiple")
    else :
      print("factor")
  else:
    print("neither")