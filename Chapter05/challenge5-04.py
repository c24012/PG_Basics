#自分の特徴を表す辞書
my_dic = {"誕生日":"8/27","身長":168,"血液型":"A型","性格":"超適当かこだわりまくるか"}

key = input("キーを入力してください:")

if key in my_dic:
    print(f"{key}は{my_dic[key]}です")
else:
    print("キーが存在しません")
