N=int(input())

S0_list=[]
S1_list=[]
S2_list=[]
S3_list=[]
T_list=[]
countlist=[0,0,0,0]

for _ in range(N):
    itigyou = list(input())
    S0_list.append(itigyou)


S1_list=[list(row) for row in zip(*S0_list[::-1])]
S2_list=[row[::-1] for row in S0_list[::-1]]
S3_list=[list(row)[::-1] for row in zip(*S0_list)]




for i in range(0,N):
    itigyou=list(input())
    T_list.append(itigyou)


def differntcount(matrix):
    count=0
    for i in range(N):
        for j in range(N):
             if matrix[i][j] != T_list[i][j]:
                 count+=1
    return count

countlist[0]=0+differntcount(S0_list)
countlist[1]=1+differntcount(S1_list)
countlist[2]=2+differntcount(S2_list)
countlist[3]=3+differntcount(S3_list)


print(min(countlist))