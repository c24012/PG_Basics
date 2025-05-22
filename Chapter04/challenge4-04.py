def remainder(x):
    """
    引数xを2で割った値(整数)を返す関数

    引数:
        x : int
    戻り値:
        result : int
    """

    result = x // 2
    return result

def quad(x):
    """
    引数xを4倍した値を返す関数
    
    引数:
        x : int
    戻り値:
        result : int
    """

    result = x * 4
    return result

#main
n = input("整数を入力してください")
try:
    n = int(n)
    n = remainder(n)
    print(quad(n))
except ValueError:
    print("整数以外が入力されました")
