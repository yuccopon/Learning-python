# Learning-python

## 1. Pythonのインストール
## 2. 
## x. バージョンの確認

```shell
python --version
```

## 実行方法

```shell
python main.py
```

# 数字を入力させる方法

##　input() を使う
###　input() 関数は、ユーザーからの入力を受け取るために使用されます。

### 数字の場合

```python
num = input("数字を入力してください:")
print("あなたが入力した数字は", num, "です。")
```

###　文字列の場合
#### input() 関数で入力した文字列を変数 string に代入し、
変数 string を print()関数で出力します。

```python
string = input("数字を入力してください:")
print("あなたが入力した数字は", string, "です。")
```

数字を入力してください: ぱいそん
あなたが入力した数字は ぱいそん です。


### （参考サイト）https://www.python.jp/train/string/input.html


# 偶数か奇数かを判定する方法

```python
num = int(input('整数を入力してね＞'))
if num % 2 == 0:
     print('あなたが入力した数字は偶数です。')
else:
     print('あなたが入力した数字は奇数です。')
```
### （参考サイト）https://www.relief.jp/docs/python-is-odd-is-even.html

## int() とは？
###　int() 関数は、入力した文字列を整数に変換します。
###　（参考サイト）https://www.javadrive.jp/python/function/index3.html



# 数字を入力させ、「0」「1」「2」...「入力した数字」を表示する方法

```python
num = int(input('整数を入力してください'))
for i in range(num + 1):
    print(i)   
```

## for文とは？
### Pythonにおけるfor文は要素を順番に取り出して処理を行うための制御構文です。
### （参考サイト）https://techplay.jp/column/1703#:~:text=Python%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8Bfor%E6%96%87%E3%81%AF%E3%80%81%E3%83%AA%E3%82%B9%E3%83%88%E3%82%84%E3%82%BF%E3%83%97%E3%83%AB%E3%80%81%E8%BE%9E%E6%9B%B8%E3%80%81,%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82

## iとは？
### ループ変数は、for文で繰り返し処理を行うために使用される変数です。

## range() とは？
### range() 関数は、指定された範囲の整数を生成するために使用されます。
####　例：range(5) は 0, 1, 2, 3, 4 を生成します。　（5回繰り返し処理を行います。）
### （参考サイト）https://www.kaijo-academy.jp/joho/py24.html#:~:text=range%E9%96%A2%E6%95%B0%E3%81%AF%E3%80%81range(n,i%E3%81%8C%E7%94%A8%E3%81%84%E3%82%89%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82


#　URLを入力させ、サイトを表示する方法

```python
import webbrowser
url = input('URLを入力してください')
webbrowser.open(url)
```
## webbrowser とは？
### 特定のWebページを開くには、webbrowser.open関数を使います。
### (参考サイト)https://qiita.com/sastrum/items/518579bc00dfae3cd293

## 数値を好きなだけ入力させて、その平均と今まで入力した数値を表示させる方法

```python
a = []
fin = False
while not fin:
    num = input("整数を入力してください。終了はfを入力してください。")
    if num == "f":
        fin = True
    else:
        a.append(int(num))
        print("あなたが入力した値は", a, "です。")

print("あなたが入力した値は", a, "です。")
print("あなたが入力した値の平均は", sum(a) / len(a), "です。")     
```


# クラスの作成方法

## クラスとはひな形
### クラスとは、オブジェクトのひな形です。

##　クラスからユーザー作成する
### 実際に作成するには、クラスをインスタンス化します。
例
user = User("John", 20)
↑　　　　↑
↑　　　クラス
インスタンスが格納された変数

※整数はクラスで、具体的な１とか２とかがインスタンス。

##　インスタンス化するときに自動的に呼び出される関数がコンストラクタ


```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.favnumbers = []
```            
