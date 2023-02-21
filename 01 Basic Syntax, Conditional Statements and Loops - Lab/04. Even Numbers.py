n = int(input())

for i in range(n):
    element = int(input())
    if element % 2 != 0:
        print(f"{element} is odd!")
        break
else:
    print("All numbers are even.")