# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# 1. Ask the user for string input.
string_input = input("Input any string: ")
final_string = ""
# 2. Access the characters in the string.
for char in string_input:

# 3. Check if any character is uppercase.
# 4. Convert the uppercase characters to lowercase by adding 32 because that is the difference between upper and  lowercase. 
    if "A" <= char <= "Z":
        final_string += chr(ord(char) + 32)
    else:
        final_string += char
# 5. Print the final string.
print(final_string)