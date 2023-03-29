numbers = [int(x) for x in input().split()]
count = int(input())

for i in range(count):
    min_number = min(numbers)
    numbers.remove(min_number)

for idx in range(len(numbers)):
    num = numbers[idx]
    if idx == len(numbers) -1:
        print(num)
    else:
        print(num, end=", ")

# list_numbers = input().split(" ")
# to_remove = int(input())
# final = []
# hui = []
#
# for i in list_numbers:
#     final.append(i)
#     final.sort(reverse=True)
#
# for t in range(to_remove, -1):
#     final.pop()
# print(final)