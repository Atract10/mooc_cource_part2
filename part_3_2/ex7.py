"""
Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string:
"""

string = input("Please type in a string: ")
len_of_str = len(string)
dash = "-"

while len_of_str != 0:
    print(string)
    print(dash * len_of_str)
    string = input("Please type in a string: ")
    len_of_str = len(string)
