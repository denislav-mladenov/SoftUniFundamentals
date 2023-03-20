number = int(input())
word = input()
listt = []
final = []

for i in range(number):
    strings = input()
    listt.append(strings)

    if word in strings:
        final.append(strings)

print(listt)
print(final)