number = int(input())


for i in range(number):
    input_string = str(input())

    is_pure = True
    for l in (input_string):

        if l == "," or l == "." or l == "_":
            is_pure = False
            break

    if is_pure == False:
        print(f"{input_string} is not pure!")
    else:
        print(f"{input_string} is pure.")



