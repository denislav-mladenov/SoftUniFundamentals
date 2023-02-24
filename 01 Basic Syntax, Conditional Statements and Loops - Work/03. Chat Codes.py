messages = int(input())

for k in range (messages):
    input_line = int(input())
    if input_line == 88:
        print("Hello")
    elif input_line == 86:
        print("How are you?")
    elif input_line < 88:
        print("GREAT!")
    else:
        print("Bye.")
