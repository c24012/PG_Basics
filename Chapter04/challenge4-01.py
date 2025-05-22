def f(x):
    return x ** 2

n = input("整数を入力してください")
try:
    n = int(n)
    print(f(n))
except ValueError:
    print("整数以外が入力されました")
