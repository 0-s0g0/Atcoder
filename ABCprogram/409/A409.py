N = int(input())
A = list(map(int, input().split()))


for k in range(N, -1, -1):
    count = sum(1 for a in A if a >= k)
    if count >= k:
        print(k)
        break
