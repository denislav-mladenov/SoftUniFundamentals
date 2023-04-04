strings = input()
to_not_use = ['a', 'o', 'u', 'e', 'i']
final = [char for char in strings if char.lower() not in to_not_use]

# for char in strings:
#     if char.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         final.append(char)
print("".join(final))