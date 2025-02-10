def convert(s):
    a = ""
    for i in s:
        if i.isalpha():  # Check if character is alphabetic
            if i.isupper():
                a += i.lower()
            elif i.islower():
                a += i.upper()
        elif i.isdigit():  # Check if character is numeric
            a += i
        else:  # For special characters
            a += i
    return a

s = input("Enter a string: ")
print("Converted String:", convert(s))

o/p:

Enter a string: Abc123
Converted String: aBC123

