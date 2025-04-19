

def call(n):
    for i in range(1,n+1):
        if i%3==0 or str(i).count("3")>=1:
            print(" %d"%(i))
    print("")

V = int(input())
call(V)