N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
sum_A_sq = sum(x**2 for x in A)
ans = (sum_A * sum_A - sum_A_sq) // 2 

print(ans)