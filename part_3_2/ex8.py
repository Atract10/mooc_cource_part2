"""
Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Sample output
Please type in a string: python

**************python
Sample output
Please type in a string: alongerstring

*******alongerstring
Sample output
Please type in a string: averyverylongstring

*averyverylongstring
"""

string = input("Please type in a string: ")
lenght_with_stars = 20
str_len = len(string)
amount_of_stars = lenght_with_stars - str_len
star = "*"
print(f"{star * amount_of_stars}{string}")