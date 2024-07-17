import math
N=246912
b=[True for i in range(N+1)]
for i in range(2,int(math.sqrt(N))+1):
    if b[i]==True:
        j=2
        while i*j <=N:
            b[i*j] = False
            j+=1
while True:
    a=int(input())
    if a==0:
        break
    cnt=0
    for i in range(a+1,a*2+1):
        if b[i]:
            cnt+=1
    print(cnt)