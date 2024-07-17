T=int(input())

for i in range(T):
    x,y=map(int,input().split())
    k=0 
    cnt=0
    i=0 
    while y-x>0: 
        i=i+1  
        if i%2!=0: 
            if k<(y-x):
                cnt=cnt+1
                k=k+1
                x=x+k
            elif k>(y-x):
                cnt=cnt+1
                k=k-1
                x=x+k
            elif k==(y-x):
                cnt=cnt+1
                x=x+k  
        if i%2==0: 
            cnt=cnt+1 
            y=y-k
    print(cnt)           