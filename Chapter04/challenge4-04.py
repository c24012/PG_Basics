def remainder(x):
    """
    Return: x % 2.
    :param x: int.
    :return: 引数xを2で割った値(整数)を返す.
    """

    return x // 2

def quad(x):
    """
    Return: x * 4.
    :param x: int.
    :return: 引数xを4倍した値を返す.
    """

    return x * 4

#main
n = input("整数を入力してください")
try:
    n = int(n)
    n = remainder(n)
    print(quad(n))
except ValueError:
    print("整数以外が入力されました")
