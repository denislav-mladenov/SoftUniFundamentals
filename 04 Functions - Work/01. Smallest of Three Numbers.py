def smallest(numbers):
    min_number = float("inf")
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest([num1, num2, num3]))