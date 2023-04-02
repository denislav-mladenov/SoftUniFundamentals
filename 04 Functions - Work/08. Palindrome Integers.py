numbers = [int(x) for x in input().split(", ")]
check = []
for el in numbers:
    check = str(el)
    if check[0] == check[-1]:
        print("True")
    else:
        print("False")

