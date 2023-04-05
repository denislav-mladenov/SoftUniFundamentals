from math import ceil

numbers = [int(x) for x in input().split(", ")]

low = 1
high = 10

group_count = ceil(max(numbers) / 10)

for idx in range (1, group_count + 1):
    grouped_nums = [x for x in numbers if low <= x <= high]
    print(f"Group of {10 * idx}'s: {grouped_nums}")

    low += 10
    high += 10