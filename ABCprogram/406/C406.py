N = int(input())
P = list(map(int, input().split()))

ABlist=[]

countA=0
countB=0

for i in range(0, N):
    if i==0:
        if P[0]<P[1]:
            ABlist.append('C')
        else:
            ABlist.append('D')
    elif i==N-1:
        ABlist.append('D')
    else:
        if P[i-1]<P[i]>P[i+1]:
            ABlist.append('A')
            countA+=1
        elif P[i]<P[i+1]:
            if P[i-1]>  P[i]:
                ABlist.append('B')
                countB+=1
            else:
                ABlist.append('C')
        else:
            ABlist.append('D')
print(ABlist)

if countA==0 or countB==0:
    print(0)
count=0
countL=0
countAA=0
countAB=0
for j in range(0,N-3):
    if ABlist[j]=='C':
        n=j
        countL=0
        while countAA==1 and countAB==1:
            if ABlist[n+1]=='A':
                countAA+=1
                n+=1
                countL+=1
            elif ABlist[j+1]=='B':
                countAB+=1
                n+=1
                countL+=1
            else:
                countL+=1
                n+=1
        if countL>=4:
            count+=1
        else:
            count+=0
