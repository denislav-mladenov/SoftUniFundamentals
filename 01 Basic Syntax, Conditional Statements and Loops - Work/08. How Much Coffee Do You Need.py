counter = 0

while True:
    word = input()
    if word == "END":
        break

    if word == "coding" or word == "dog" or word == "cat" or word == "movie":
        counter += 1
    elif word == "CODING" or word == "DOG" or word == "CAT" or word == "MOVIE":
        counter += 2

if counter > 5:
    print("You need extra sleep")
else:
    print(counter)
