text = input()
value = 0

for character in text:
    if character == "a":
        value += 1
    elif  character == "e":
        value += 2
    elif character == "i":
        value += 3
    elif character == "o":
        value += 4
    elif character == "u":
        value += 5

print(value)
