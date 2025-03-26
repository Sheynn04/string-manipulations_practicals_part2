# Objective: Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# 1. Ask  the user to input anything with spaces at the front.
string_input = input("Input anything with spaces on the front: ")

# 2. Create a loop so we can access each character in the input 
for i, char in enumerate(string_input):