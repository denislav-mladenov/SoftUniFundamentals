def even_odd_sum(numbers):
    even_sum = 0
    odd_sum = 0
    for num_str in number:
        num_int = int(num_str)
        if num_int % 2 == 0:
            even_sum += num_int
        else:
            odd_sum += num_int
    return (f"Odd sum = {odd_sum}, Even sum = {even_sum}")

number = input()
print(even_odd_sum(number))