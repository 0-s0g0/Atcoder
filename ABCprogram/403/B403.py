A=list(input())
B=list(input())

LENA=len(A)
LENB=len(B)
countA=0
if LENA==4:
    print('Yes')

else:
    for i in range(0,len(A)):
        if A[i]!='?':
            for j in range(0,LENB):
                if i>=j:
                    if A[i]==B[j]:
                        count=0
                        lenA=[]
                        lenB=[]
                        
                        for k in range(0,LENB):
                            if (A[i-j+k]==B[k]) or (A[i-j+k]=='?'):
                                lenA.append(A[i-j+k])
                                lenB.append(B[k])
                                count+=1
                        if count==LENB:
                            countA+=1
    if countA==0:
        print('No')
    else:
        print('Yes')