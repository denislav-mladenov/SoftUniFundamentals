number_of_snowballs = int(input())

best_snowball = 0
output = ''

for i in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality= int(input())


    snowball_value = (snowball_weight // snowball_time) ** snowball_quality

    if snowball_value > best_snowball:
        best_snowball = snowball_value
        output = f"{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"

print(output)
