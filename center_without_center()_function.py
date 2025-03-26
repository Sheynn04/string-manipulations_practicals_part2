# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# 1. Ask for user input. 
string_input = input("Input any string: ")
width = 100

# 2. Add spaces equally on both sides if length of string is less that width
if len(string_input) < width:
    spaces = (width - len(string_input)) // 2
    string_input = " " * spaces + string_input + " " * (width - len(string_input) - spaces)

# 3. Print the centered string
print(string_input)