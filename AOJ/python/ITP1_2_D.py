w,h,x,y,r=map(int,input().split())

if(r<=y<=h-r)and (r<=x<=w-r):
    print("Yes")
else:
    print("No")