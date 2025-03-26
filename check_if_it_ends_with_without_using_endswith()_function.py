# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# 1. Ask for user input.
string_input = input("Input any string:  ")

# 2. Assign a suffix.
ends_with = "dy"

# 3. Check if the input ends with the suffix.
# 4. Print True if yes, False if not.
if string_input[-len(ends_with):] == ends_with:
    print("True")
else:
    print("False")