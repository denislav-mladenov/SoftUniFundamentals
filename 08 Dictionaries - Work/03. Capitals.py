countries = input().split(", ")
capitals = input().split(", ")

capital_by_country = {}

for idx in range(len(countries)):
    country = countries[idx]
    capital = capitals[idx]
    capital_by_country[country] = capital

for country, capital in capital_by_country.items():
    print(f"{country} -> {capital}")