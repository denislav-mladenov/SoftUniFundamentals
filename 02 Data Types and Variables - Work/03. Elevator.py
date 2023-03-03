number_people = int(input())
capacity_people = int(input())

courses = (number_people + capacity_people - 1) // capacity_people

print(courses)