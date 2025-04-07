"""
B - Full House 3
【リストの要素数を計算する辞書型】
問題文
7 枚のカードがあります。i 番目 (i=1,…,7) のカードには整数 Ai が書かれています。
これらのカードから 5 枚を選び、フルハウスとできるか判定してください。
ただし、 5 枚組のカードは以下の条件を満たすとき、またそのときに限って、フルハウスであると呼ばれます。
・異なる整数 x,y について、x が書かれたカード 3 枚と y が書かれたカード 2 枚からなる。
制約
Ai  は 1 以上 13 以下の整数
"""

# 入力を受け取る
a = input().split()#1 4 1 4 2 1 3(数字と空白が混ざった値)

# 辞書で出現回数を数える
count_dict = {}#空の辞書

for card in a:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1
#count_dict:{'1': 3, '4': 2, '2': 1, '3': 1}

# 出現回数だけのリストを作る
counts = list(count_dict.values())
#counts:[3, 2, 1, 1]
counts.sort()
counts.reverse()
#print(counts)
# フルハウスの条件を満たすかチェック（3が1回、2が1回）
if len(counts)>=2:
    if counts[0] >= 3 and counts[1]>=2:
        print("Yes")
    else:
        print("No")
else:
    print("No")


