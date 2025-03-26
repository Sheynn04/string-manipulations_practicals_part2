# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# 1. Ask for user input.
string_input = input("Input any string: ")

# 2. Reverse the casing of each character.
swapped_string = ""
for char in string_input:
    if "A" <= char <= "Z":  # If uppercase, convert to lowercase
        swapped_string += chr(ord(char) + 32)
    elif "a" <= char <= "z":  # If lowercase, convert to uppercase
        swapped_string += chr(ord(char) - 32)
    else:
        swapped_string += char  # Keep non-alphabet characters the same