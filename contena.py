# python /Users/hirano.wataru/be_professional_python/contena.py
# coding: utf_8

# メソッドはrubyと同じくかなり豊富に提供されている。
print("hello".upper())


# リスト
fruits = list()
print(fruits)
fruits.append("apple")
fruits.append("banana")
fruits.append("mango")
# ruby 形式の << は使えないappend だけっぽい。
# fruits << "banana"
print(fruits)

# インデックスに無い、数字を指定してしまうとrubyと違い、indexerrorが表示されてしまう。
# print(fruits[3])
# -> IndexError: list index out of range

# 最後の要素を削除したいときはpop、でも、このpopは強制的にもともとの変数に作用する。（rubyは！が必要だが。）
last_words = fruits.pop()
print(last_words)
print(fruits)

# 含まれているか、確認するときは、inを使用する。
# notも使えるよ。
print ("banana" in fruits)
print ("banana" not in fruits)

# 要素の数を数えたいときは、
print(len(fruits))



#####重要　pythonにはタプルと呼ばれるものがある。
# タプルとは、listと違い、一度定義してしまうと、変更不可のアイテムです。

# list
friend_list = ["wataru", "bhharath", "yoko"]
# tuple
unbrakable_frined_list = ("wataru", "bhharath", "yoko")

# タプルはリストの追加ができない。
# unbrakable_frined_list.append("shiva")
#=> AttributeError: 'tuple' object has no attribute 'append'

#################################################################################################


#dictionary
# rubyで言うところのhashである。
# 使用方法はほぼ変わらない。
jisho = dict()
print(jisho)

jisho['広辞苑'] = "heavy"
jisho['google_honyaku'] = "karui"
jisho.append("no")
print(jisho)



