# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# 1. Assign a prefix.
prefix = "ycz"

# 2. Ask the user for string input.
string_input = input("Input any string: ")

# 3. Use .startswith() function to remove the prefix we assigned earlier
if string_input.startswith(prefix):

# 4. Print the string without the prefix
    print(string_input[len(prefix):])

else:
    print(string_input)