# def ascii_range(char1, char2):
#     char1 = ord(char1)
#     char2 = ord(char2)
#     char_range = range(min(char1, char2) + 1, max(char1, char2))
#     return ' '.join([chr(char) for char in char_range])
#
#
# ch1 = input()
# ch2 = input()
# print(ascii_range(ch1, ch2))


def ascii_range(start, end):
    result = []
    for num in range(ord(start) + 1, ord(end)):
        result.append(chr(num))

    return result

start_chart = input()
end_chart = input()

result_char = ascii_range(start_chart, end_chart)
print(" ".join(result_char))