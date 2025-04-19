a=1
b=1

while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    else:
        if a<b:
            print("%d %d"%(a,b))
        else:
            print("%d %d"%(b,a))