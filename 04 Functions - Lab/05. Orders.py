def shop(product, quantity):
    total_money = 0
    if product == "coffee":
        total_money = quantity * 1.50
    elif product == "water":
        total_money = quantity * 1.00
    elif product == "coke":
        total_money = quantity * 1.40
    elif product == "snacks":
        total_money = quantity * 2.00
    return total_money


product = input()
quantity = int(input())
result = shop(product,quantity)
print(f"{result:.2f}")