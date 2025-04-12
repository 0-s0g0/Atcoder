n=int(input())
A = [input() for _ in range(n)]

#print(n)
#print(A)

login_count=0
logout_count=0
private_count=0
public_count=0
error_count=0

for word in A:
    if word=='login':
        login_count+=1
    elif word=='logout':
        login_count=logout_count
    elif word=='private':
        if login_count==0:
            error_count+=1
        else:
            public_count+=1
    else:
        public_count+=1
    

print(error_count)


