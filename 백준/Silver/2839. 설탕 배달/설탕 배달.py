a=int(input())
cnt3=0
cnt5=0
while True:
    if a%5 !=0 :
        if a>0:
            cnt3=cnt3+1
            a=a-3
        if a==0:
            print(cnt3)
            break
        if a<0 :
            print("-1")
            break
    elif a % 5 ==0 :
        if a>0:
            cnt5=a/5
            print(int(cnt3+cnt5))
            break
        if a==0:
            print("-1")
            break