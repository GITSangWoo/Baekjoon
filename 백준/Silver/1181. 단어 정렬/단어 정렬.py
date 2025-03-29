N=int(input())
word={}
# 딕셔너리 활용 길이에 따라 단어 분류 1:[i,u] 2:[am]
for _ in range(N):
  w=input()
  if len(w) not in word:
    word[len(w)]=[]
  word[len(w)].append(w)

# 중복제거하면서 sort()활용
for key,value in sorted(word.items()):
  value=list(set(value))
  value.sort()
  for i in range(len(value)):
    print(value[i])