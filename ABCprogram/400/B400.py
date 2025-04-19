b, c = map(int, input().split())

sum=0
for i in range(0,c+1):
    po=b**i
    sum+=po
if sum<=10**9:
        print(sum)
else:
    print("inf")
