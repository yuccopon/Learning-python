
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

