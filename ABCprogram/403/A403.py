A=int(input())
B=list(map(int,input().split()))

ans=0
count=1
for i in range(0,A):
    if i%2==0:
        ans+=B[i]

print(ans)