while True:
    word = input()
    if word == "SoftUni":
        continue
    if word == "End":
        break
    for l in word:
        print(f"{l}{l}", end="")
    print()
