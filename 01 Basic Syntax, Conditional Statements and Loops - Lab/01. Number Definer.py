a = float(input())

if a == 0:
    print("zero")
elif a >= 1 and a <= 999999:
    print("positive")
elif a < 1 and a > 0:
    print("small positive")
elif a >= 1000000:
    print("large positive")
elif abs(a) >= 1 and abs(a) <= 999999:
    print("negative")
elif abs(a) < 1 and abs(a) > 0:
    print("small negative")
elif abs(a) >= 1000000:
    print("large negative")