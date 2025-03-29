# 회원 수 입력받기
N=int(input())
# 회원 딕셔너리 생성
mem={}
# 나이를 키 회원이름을 값으로 받아서 저장 
for _ in range(N):
  age,name=input().split()
  age=int(age)
  if age not in mem:
    mem[age]=[]
  mem[age].append(name)

# 나이는 정렬, 같은 나이는 먼저 가입한 순서대로이므로 그대로
for key,value in sorted(mem.items()):
  for i in range(len(value)):
    print(f"{key} {value[i]}")