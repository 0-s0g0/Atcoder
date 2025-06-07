N,M =map(int, input().split())
A =list(map(int, input().split()))
B=list(i for i in range(1,M+1))
C=list(i for i in range(1,M+1))
#print(B)
count=N
#print(C)
for i in B:
    for j in range(N-1,0,-1):
        if i==A[j]:
            #print(i,'は',j,'にある')
            if count>(j):
                count=j
                #print(i,j,count,'更新')
                C.remove(i)
                #print('Cは',C)
                #print('Bは',C)
            else:
                count==count
                C.remove(i)
                #print(i,j,count,'not更新')
                #print('Cは',C)
                #print('Bは',C)
            break
#print(count_B)
if len(C)==0:
    print(count)
else:
    print(0)