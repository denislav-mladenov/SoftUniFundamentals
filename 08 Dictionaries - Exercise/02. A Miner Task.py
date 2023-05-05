resources = {}

while True:
    mineral = input()
    if mineral == "stop":
        break

    quantity = int(input())
    if mineral in resources:
        resources[mineral] += quantity
    else:
        resources[mineral] = quantity

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")