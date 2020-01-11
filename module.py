# python3 /Users/lawrie_6strings/be_professional_pythonist/module.py
# -*- coding: utf-8 -*-

# 1.
import statistics
average = [1,2,3,4,5,8,9,0,6,5]
print(statistics.mode(average))

# 2.
# 同じ名前のファイルとフォルダがある場合は、ライブラリとモジュールのディレクトリを認識させるために、__init__.pyが必要らしい。
from module import cubed

print(cubed.cubed(100))

