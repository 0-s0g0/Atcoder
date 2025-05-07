N,M=map(int, input().split())
A=[]

for i in range(M):
    input_row=list(map(int,input().split()))
    A.append(input_row)

B_row=list(map(int,input().split()))
#print(A)
#print(B_row)

for j in B_row:
    count=0
    for l in A:
        for m in range(1,len(l)):
            if j==l[m]:
                l.pop(m)
                break
        if len(l)==1:
            count+=1
        #print(j,l)

    print(count)           



