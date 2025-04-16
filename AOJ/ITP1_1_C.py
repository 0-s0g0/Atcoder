a=list(map(int, input().split()))
ans_list=[]

L=a[0]*2+a[1]*2


S=a[0]*a[1]
ans_list.append(S)
ans_list.append(L)
result = ' '.join(map(str, ans_list))
print(result)