number_cities = int(input())
total_profit = 0

for i in range(1, number_cities + 1):
    name_of_city = input()
    owner_income = float(input())
    owner_expenses = float(input())

    if i % 3 == 0 and i % 5 != 0:
        owner_expenses *= 1.5
    if i % 5 == 0:
        owner_income *= 0.9

    profit = owner_income - owner_expenses
    total_profit += profit
    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")