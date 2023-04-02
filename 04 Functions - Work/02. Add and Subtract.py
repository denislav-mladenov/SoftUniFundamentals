# def add_and_subtract(a, b, c):
#     sum = sum_numbers(a, b)
#     result = subtract(a, b, c)
#     return result
#
# def sum_numbers(a, b):
#     return a + b
#
# def subtract(a, b, c):
#     return (a + b) - c
#
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# print(add_and_subtract(number1, number2, number3))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

number1 = int(input())
number2 = int(input())
number3 = int(input())

add = add(number1, number2)
print(subtract(add, number3))