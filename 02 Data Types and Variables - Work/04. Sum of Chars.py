n = int(input())
total_sum = 0
i = 0

while i < n:
    letter = input()
    total_sum += ord(letter)
    i += 1
print(f"The sum equals: {total_sum}")


# n = int(input())
# total_sum = 0
#
# for i in range(n):
#     letter = input()
#     total_sum += ord(letter)
#
# print("The sum equals:", total_sum)