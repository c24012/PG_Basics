import csv

nest_list = [
        ["Top Gun","Risky Business","Minority Report"],
        ["Titanic","The Revenant","Inception"],
        ["Training Day","Man on Fire","Flight"]
        ]

with open("challengeCSV.csv","w") as f:
    r = csv.writer(f,delimiter=",")
    for i in range(len(nest_list)):
        r.writerow(nest_list[i])
        
