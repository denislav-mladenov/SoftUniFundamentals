budget = int(input())

input_line = input()

while input_line != "End":
    current_budget = int(input_line)
    budget -= current_budget
    if budget < 0:
        print("You went in overdraft!")
        break
    input_line = input()
else:
    print("You bought everything needed.")