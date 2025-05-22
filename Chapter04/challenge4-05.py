s = input("数字を入力してください:")

try:
    f = float(s)
    print(f)
except ValueError:
    print("数字が入力されていません")
