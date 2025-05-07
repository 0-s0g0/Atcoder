N,M,Q=map(int,input().split())

ANS_ALL=[]

for i in range(0,N):
    ANS_ALL.append([])

print(ANS_ALL)

for i in range(0,Q):
    input_row=list(map(int,input().split()))
    #print(input_row)
    if input_row[0]==1:
        ANS_ALL[input_row[1]-0].append(input_row[2])
    elif input_row[0]==2:
        for j in range(0,M):
            ANS_ALL[input_row[1]-0].append(j)
    else:
        print('OK')


print(ANS_ALL)
