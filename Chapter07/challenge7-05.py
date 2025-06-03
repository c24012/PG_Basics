list1 = [8,19,148,4]
list2 = [9,1,33,83]
results = []

for i in list1:
    for j in list2:
        results += [i * j]

for n in results:
    print(n)
