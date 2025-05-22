def str_to_flo(s):
    """
    引数s(string)をfloatに変換する関数

    引数:
        s : string
    戻り値:
        f : float
    """

    try:
        f = float(s)
        return f
    except ValueError:
        print("数字が入力されていません")

#main
s = input("数字を入力してください:")
print(str_to_flo(s))
