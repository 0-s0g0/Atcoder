"""
C - Uniqueness
【リストの要素数を計算する辞書型】
問題文
1 から N の番号がついた N 人の人がいます。人 i は数 A i​  を持っています。
「自分と同じ数を持っている人が自分以外のN−1 人の中に存在しない」という条件を満たす人のうち、持っている数が最大である人の番号を求めてください。
条件を満たす人が存在しない場合、代わりにそのことを報告してください。
制約
Ai  は 1 以上 13 以下の整数
"""

# 入力を受け取る
n = int(input())
a = input().split()#2 9 9 7 9 2 4 5 8(数字と空白が混ざった値)

# 辞書で出現回数を数える
count_dict = {}#空の辞書

for card in a:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1
#count_dict:{'2': 2, '9': 3, '7': 1, '4': 1, '5': 1, '8': 1}
#print(count_dict)

one_countlist=[]
for key in count_dict:
    if count_dict[key]==1:
        one_countlist.append(key)

#print(one_countlist)
if len(one_countlist)==0:
    print(-1)
else:
    one_countlist.sort()
    one_countlist.reverse()
    max_item=one_countlist[0]
    #print(one_countlist)
    #print(max_item)
    count=1
    for i in a:
        if i==max_item:
            print(count)
            break
        else:
            count+=1
            continue
