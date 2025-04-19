s=input()
A=[]
for i in s:
    if i.isupper()==True:
        A.append(i)

print(''.join(A))