first = input().split(", ")
second = input().split(", ")

result = []

for sub in first:
    for word in second:
        check = sub in word
        if check:
            result.append(sub)
            break


print(result)