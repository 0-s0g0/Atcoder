N, K = map(int, input().split())

num_list=[]
A_list=[]


#print(num_list)
if N>K:
    for b in range(0,N+1):
        if 0<=b<K:
            A_list.append(1)
            #print('b',b,'A_list',A_list)
        else:
            count=0
            for c in range(b-K,b):
                count+=A_list[c]
                #print('b',b,'A_list',A_list,'c',c,'count',count)
            A_list.append(count)
    ans_sum=A_list[-1]

else:
    for b in range(0,N+1):
         A_list.append(1)
         
        
    ans_sum=A_list[-1]
    




    



#print(num_list)
#print(A_list)
#print(ans_sum)
print(ans_sum%(10**9))