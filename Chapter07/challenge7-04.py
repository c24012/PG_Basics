num_list = [2,3,5,7,11,13,17,19]

while True :
    n = input("数字を入力してください:")
    try:
        n = int(n)
        if n in num_list:
            print("正解")
        else:
            print("不正解")
    except ValueError:
        if n == "q":
            break
        else :
            print("数字を入力するか、qで終了します")
