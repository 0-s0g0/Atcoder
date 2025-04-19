input_list=[]
while True:
    input_list=list(input().split())
    if input_list[1]=='?':
        break
    else:
        a=int(input_list[0])
        b=int(input_list[2])
        if input_list[1]=='+':
            print("%d"%(a+b))
        elif input_list[1]=='-':
            print("%d"%(a-b))
        elif input_list[1]=='*':
            print("%d"%(a*b))
        else:
            print("%d"%(a/b))