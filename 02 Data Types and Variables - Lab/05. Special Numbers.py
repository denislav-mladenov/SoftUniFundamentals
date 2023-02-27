# def is_special(num):
#     return sum(int(digit) for digit in str(num)) in [5, 7, 11]
#
# n = int(input())
# for num in range(1, n+1):
#     print(num, "->", is_special(num))
#

# n = int(input())
#
# for i in range(1, n+1):
#     special = False
#     num = i
#     sum_of_digits = 0
#     while num > 0:
#         sum_of_digits += num % 10
#         num = num // 10
#     if sum_of_digits in [5, 7, 11]:
#         special = True
#     print(f"{i} -> {special}")

number = int(input())

for i in range(1, number + 1):
    special = False
    num_as_string = str(i)
    sum_digits = 0

    for char in num_as_string:
        sum_digits += int(char)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        special = True

    print(f"{i} -> {special}")