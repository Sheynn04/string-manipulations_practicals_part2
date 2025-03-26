# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# 1. Ask for user input.
string_input = input("Input any string: ")

# 2. Convert the first letter of each word to uppercase, others to lowercase.
title_case_string = " ".join(word[0].upper() + word[1:].lower() if word else "" for word in string_input.split())

# 3. Print the result.
print(title_case_string)
