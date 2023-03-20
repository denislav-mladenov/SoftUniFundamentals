number = int(input())
positive = []
negative = []

for i in range(number):
    current_list = int(input())
    if current_list >= 0:
        positive.append(current_list)
    else:
        negative.append(current_list)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")