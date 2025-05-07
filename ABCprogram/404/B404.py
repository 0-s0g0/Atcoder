N,M=map(int,input().split())

Enter_price=list(map(int,input().split()))

animal_list=[]

for i in range(0,M):
    animal_kaku=list(map(int,input().split()))
    animal_list.append(animal_kaku)

print(animal_list)
