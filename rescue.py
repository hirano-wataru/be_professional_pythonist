# python /Users/hirano.wataru/be_professional_python/rescue.py
# coding: utf_8


try:
    # ドキュメンテーション文字列
    # 複数行に渡って、説明を行いたい場合に使用する。
    
    """
    domucantation_string
    a is int
    b is int
    """
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)  
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("invalid exeption:")