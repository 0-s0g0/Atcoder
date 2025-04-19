H=1
W=1
asn_list=[]
while True:
    H,W=map(int,input().split())
    if H==0 and W==0:
        break
    else:
        for i in range(H):
            for j in range(W):
                if  (i+j)%2==0:
                    asn_list.append('#')
                else:
                    asn_list.append('.')
            print(''.join(asn_list))
            asn_list=[]
        print()