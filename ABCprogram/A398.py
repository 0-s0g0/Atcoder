"""
A - Doors in the Center
問題文
以下の条件を全て満たす長さ N の文字列を求めてください。

各文字は - または = である
回文である
文字列中に = は 1 個または2 個含まれる。2 個含まれる場合、それらの = は隣接している
なお、そのような文字列はちょうど1 つ存在します。

制約
1≤N≤100
N は整数である
"""

a = int(input())
ans_list=["-"]*a
#print(ans_list)
#print(a)
if a%2==0:
    manaka=int(a/2)
    ans_list[manaka]="="
    ans_list[manaka-1]="="

else:
    manaka2=int((a-1)/2)
    ans_list[manaka2]="="

ans=''.join(ans_list)


print(ans)