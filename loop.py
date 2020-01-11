# python3 /Users/lawrie_6strings/be_professional_pythonist/loop.py
# -*- coding: utf-8 -*-
# 1
array = ["ウォーキングデッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for word in array:
    print(word)

# 2
for i in range(25, 51):
    print(i)

# 3
# rubyで言う、「each_with_index」.
# for "インデックス番号", "文字列が格納される変数"　 in enumerate("リスト"もしくは"タプル")
for i, word in enumerate(array):
    print(str(i) + ":" + word)

# 4
# 数字当てゲーム
"try catchの部分で詰まってしまった。"
"パースが失敗するとエラーになるようだ。rubyでは何かしら変換できるけど。"
import random

while True:
    random_number = random.randint(1, 4)
    input_int = input("入力してください。")
    if input_int == "q":
        print("ゲームを終了します。")
        break
    try:
        answer = int(input_int)
    except ValueError:
        print("数字を入力するか、qを入力してください。")
        continue
    if int(input_int) == random_number:
        print("正解です。")
    else:
        print("不正解です。正解は{}でした".format(random_number))


# 5
array1 = [8,19,148,4]
array2 = [9,1,33,83]
array3 = []
for i, number in enumerate(array1):
    array3.append(array2[i] * number)


print(array3)
