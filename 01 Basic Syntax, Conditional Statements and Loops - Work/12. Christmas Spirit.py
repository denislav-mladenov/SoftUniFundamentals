quantity = int(input())
days = int(input())

cost = 0
spirit = 0

for day in range(1, days + 1):
    if day % 2 == 0:
        cost += 2 * quantity
        spirit += 5 * quantity

    if day % 3 == 0:
        cost += (5 + 3) * quantity
        spirit += (3 + 10) * quantity

    if day % 5 == 0:
        cost += 15 * quantity
        spirit += 17 * quantity

    if day % 3 == 0 and day % 5 == 0:
        spirit += 30

    if day % 10 == 0:
        cost += (5 + 3 + 15) * quantity
        spirit -= 20

    if day % 11 == 0:
        quantity += 2

if days % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")