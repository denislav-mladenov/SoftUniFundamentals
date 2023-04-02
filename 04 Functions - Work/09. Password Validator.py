def is_valid_lengh(password):
    return 6 <= len(password) <= 10

def contain_alpha_numeric_chars(password):
    return password.isalnum()

def contain_two_digits(password):
    digits_counter = 0
    for char in password:
        if char.isdigit():
            digits_counter += 1

    return digits_counter >= 2

input_password = input()
is_valid = True


if not is_valid_lengh(input_password):
    is_valid = False
    print("Password must be between 6 and 10 characters")
if not contain_alpha_numeric_chars(input_password):
    is_valid = False
    print("Password must consist only of letters and digits")
if not contain_two_digits(input_password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")



