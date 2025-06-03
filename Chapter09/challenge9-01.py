import os

texts = []
with open("test_memo.txt", "r") as memo:
    texts.append(memo.read())

print(texts)
