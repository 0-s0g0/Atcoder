q=int(input())
A=[]

for i in range(q):
    input_row=input()
    if input_row=='2':
        print(A[0])
        A.pop(0)
    else:
        a,b=map(int, input_row.split())
        A.append(b)