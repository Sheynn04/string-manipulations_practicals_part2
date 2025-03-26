# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# 1. Ask for the user input.
string_input = input("Enter any string: ")

# 2. Assign length of characters.
width = 100

# 3. Check if the input has the same length of characters as the width. 
# 4. Add spaces in the end if character length is less than width.
# 5. Print the ljust string.
if len(string_input) < width:
    string_input += " " * (width-len(string_input))

print(string_input)
