# python /Users/lawrie_6strings/be_professional_pythonist/control_string.py
# -*- coding: utf-8 -*-
# 文字列を３行で書いてみたい場合
"""
どないやねん。
最近の若いもんは、
ようやるやんけ。
"""

# 文字列の特定の文字を取得したい場合は,インデックスを指定してあげることでなんとかする。
word = "what's up"
print(word[0])

# 書式化
name = "lady gaga"
print("こんにちわ、私の名前は {} です。".format(name))

"複数の文字列を挿入することもできる。"
year = 1990
month = 7
day = 11
print("{}/{}/{}".format(year, month, day))

# チャレンジ
## １
for i in range(0, 5):
    print("kamyu"[i])

## 2
# what = input("what:")
# who = input("who:")
# print("I write {},I send it to {}".format(what, who))

## 3
print("aldous Huxley was born in 1894".capitalize())

## 4
print("when? what? who?".split())

## 5
"最後のピリオドを再利用しようとしすぎて、詰まってしまった。"
word = ["the", "fox", "jumped", "over", "the", "fence", "."]
word = " ".join(word)
word = word[0:-2] + "."
print(word)

## 6
print("A screeming comes across the sky.".replace("s", "$"))

## 7
print("Hemingway".index("m"))

## 8　文字列の中にさらに文字列を入れたい時。
print("ケンシロウは言った\"お前はもう死んでいる\"とな")


## 9
print("アタタタ,"*10 + "オワッター！")

## 10
print("４月の晴れた寒い日で、時計がどれも十三時を打っていた。".split("、")[0])