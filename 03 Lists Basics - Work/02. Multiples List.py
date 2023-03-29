factor = int(input())
count = int(input())
listt = []

final = 0
for i in range(0, count):
    final += int(factor)
    listt.append(final)

print(listt)