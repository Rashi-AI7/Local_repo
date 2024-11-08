print("Hello World!!")
print("Welcome!")
print("to the *Palindrome Checker*.")
# rules
print("Here are the rules and instructions that you need to use the *Palindrome Checker*:")
print("1. Enter a valid set of string or integer.")
print("2. If the machine returns wrong answer, keep calm as mistakes are common.")
print("3. Enjoy checking if your name, age, your family member's name, your friend's name, your school name your roll no., and your region's postal code if they are palindromic or not.")
print("Disclaimer: If you do not know about palindromes, don't worry and when the machine asks you for the string, type /palindrome for knowing about it.")

# important functions


# palindrome checker function
def is_palindrome(s):
    # Remove spaces and make lowercase for accurate comparison
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# take input

def takeinput():
    string = input("Enter the string: ")
    return string
    


# check if palindrome

def checkifpalindrome(string):
    if "/" in string:
        return "Palindromes are the sets of integers and alphabets that are read the same from left to right and right to left. For example, '12abcba21' is a palindrome."
    elif is_palindrome(string):
        return "The string is a palindrome!"
    else:
        print("The string is not a palindrome!")

# call the functions

print(checkifpalindrome(takeinput()))

# a function for running the program until the user wants

choice = input("Do you want to check another string? (yes/no): ").strip().lower()
if choice != 'yes':
        print("Exiting the palindrome checker.")
