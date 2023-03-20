number = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for i in range(number):
    random_numbers = int(input())

    if random_numbers % 2 == 0:
        even_list.append(random_numbers)
    else:
        odd_list.append(random_numbers)

    if random_numbers >= 0:
        positive_list.append(random_numbers)
    else:
        negative_list.append(random_numbers)


word = input()

if word == "even":
    print(even_list)
elif word == "odd":
    print(odd_list)
elif word == "negative":
    print(negative_list)
elif word == "positive":
    print(positive_list)