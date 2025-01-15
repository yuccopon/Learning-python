# 文字列を出力する
print ("Hello, World!")

# 数字を出力する
num = input("数字を入力してください:")
print("あなたが入力した数字は", num, "です。")

# 偶数か奇数かを判定する
num = int(input('整数を入力してください'))
if num % 2 == 0:
     print('あなたが入力した数字は偶数です。')
else:
     print('あなたが入力した数字は奇数です。')

#　Pythonで数字を入力させ、「0」「1」「2」...「入力した数字」を表示する。
num = int(input('整数を入力してください'))
for i in range(num + 1):
    print(i)    

# URLを入力させ、サイトを表示する方法
import webbrowser
url = input('URLを入力してください')
webbrowser.open(url)


