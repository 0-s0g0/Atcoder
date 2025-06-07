N, K =map(int, input().split())
A =list(map(int, input().split()))

pro=1
for i in A:
    pro=i*pro
    if len(str(pro))>K:
        pro=1

print(pro)
