employess = input().split(" ")
happiness_factor = int(input())

employess = list(map(lambda x: int(x) * happiness_factor, employess))

filtered = list(filter(lambda x: x >= (sum(employess) / len(employess)), employess))

if len(filtered) >= len(employess) / 2:
    print(f"Score: {len(filtered)}/{len(employess)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employess)}. Employees are not happy!")