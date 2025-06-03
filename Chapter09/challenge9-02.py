food = input("何の食べ物が好き？:")

with open("like_food.txt","w") as f:
    f.write(f"好きな食べ物は「{food}」\n")
