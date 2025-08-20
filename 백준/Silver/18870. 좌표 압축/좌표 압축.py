# 좌표의 개수 받기
N = int(input())
# 좌표를 리스트로 받고 작은 순서대로 정렬하기 정렬하기 전 좌표값을 b에 저장
a = list(map(int, input().split()))
b = a.copy()
a = list(set(a))
a.sort()

# 딕셔너리를 활용하여 값을 키로, 키를 값으로 저장
comp_code = {v: i for i, v in enumerate(a)}

# 처음 입력받은 좌표 리스트 b의 순서대로 해당값이 속한 키값을 출력
for i in b:
  print(comp_code[i], end=" ")