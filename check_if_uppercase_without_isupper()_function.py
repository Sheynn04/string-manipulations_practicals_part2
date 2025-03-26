# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# 1. Ask the useer to input.
string_input = input("Input any string: ")

# 2. Assign true to uppercase letters.
is_upper = True

# 3. Access each character in the input.
for char in string_input:

# 4. Check if characters are upper. If yes print true, if no print false.
    if not ("A" <= char <= "Z"):
        is_upper = False
        break
print(is_upper)

