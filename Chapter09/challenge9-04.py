import csv

nest_list = [
        ["トップガン","リスキー ビジネス","マイノリティ・リポート"],
        ["タイタニック","レヴェナント","インセプション"],
        ["トレーニング デイ","マイ・ボディガード","フライト"]
        ]

with open("challengeCSV_jp.csv","w") as f:
    r = csv.writer(f,delimiter=",")
    for i in range(len(nest_list)):
        r.writerow(nest_list[i])
 
