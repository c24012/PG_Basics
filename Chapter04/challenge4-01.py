def f(x):
    """
    引数xを２乗した値を返す関数

    引数:
        x : int

    戻り値:
        result : int
    """

    result = x ** 2
    return result

n = input("整数を入力してください")
try:
    n = int(n)
    print(f(n))
except ValueError:
    print("整数以外が入力されました")
