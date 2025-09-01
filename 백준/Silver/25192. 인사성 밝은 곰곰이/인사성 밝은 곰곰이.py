N = int(input())
result = 0
l=set([])
for _ in range(N):
  chat = input()
  if chat == "ENTER":
    result += len(l)
    l.clear()
  else :
    l.add(chat)

result += len(l)
print(result)