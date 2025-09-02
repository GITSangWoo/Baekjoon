import sys 
N = int(sys.stdin.readline())
l=[]
for _ in range(N):
  l.append(int(sys.stdin.readline()))

l.sort()
# 산술평균 
print(int(round(sum(l)/len(l),0)))
# 중앙값
print(l[int(len(l)//2)])
# 최빈값
numcnt = {}
for i in l:
  numcnt[i]=numcnt.get(i,0)+1

count_map={}
for num,cnt in numcnt.items():
  if cnt in count_map:
    count_map[cnt].append(num)
  else: 
    count_map[cnt] =[num]
maxcount = max(count_map.keys())
if len(count_map[maxcount])>1:
  result = sorted(count_map[maxcount])[1]
  print(result)
else:
  result = count_map[maxcount][0]
  print(result)
# 범위 
if N > 1:
  print(l[-1]-l[0])
else:
  print(0)