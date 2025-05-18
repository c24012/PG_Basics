age = 21
now = 2025

print("入力年齢:(満)" + str(age) + "歳")

whitch = None

if age < 18:
    whitch = "未成年"
else:
    whitch = "成年済み"

print(str(age) + "は" + str(now - age) + "年生まれで" + whitch + "です")
