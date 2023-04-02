def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

perfect_number = int(input())
print(is_perfect(perfect_number))