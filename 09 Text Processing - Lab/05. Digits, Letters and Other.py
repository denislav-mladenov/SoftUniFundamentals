text = input()

letters = ""
digits = ""
symbols = ""

for chr in text:
    if chr.isalpha():
        letters += chr
    elif chr.isdigit():
        digits += chr
    else:
        symbols += chr


print(digits)
print(letters)
print(symbols)