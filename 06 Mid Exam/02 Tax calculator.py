vehicles = [x for x in input().split(">>")]
total_tax_collected = 0

for x in vehicles:
    vehicle_data = x.split(" ")
    car = vehicle_data[0]
    in_use = int(vehicle_data[1])
    traveled_km = int(vehicle_data[2])

    if car == "family":
        init_tax = 50
        tax_per_year = 5
        tax_per_km = 12
        total_tax = init_tax - (tax_per_year * in_use) + (tax_per_km * (traveled_km // 3000))
    elif car == "heavyDuty":
        init_tax = 80
        tax_per_year = 8
        tax_per_km = 14
        total_tax = init_tax - (tax_per_year * in_use) + (tax_per_km * (traveled_km // 9000))
    elif car == "sports":
        init_tax = 100
        tax_per_year = 9
        tax_per_km = 18
        total_tax = init_tax - (tax_per_year * in_use) + (tax_per_km * (traveled_km // 2000))
    else:
        print("Invalid car type.")
        continue

    total_tax_collected += total_tax
    print(f"A {car} car will pay {total_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
