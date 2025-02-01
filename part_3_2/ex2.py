"""
Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer

Sample output
Please type in string 1: howdy doody
Please type in string 2: hola
howdy doody is longer

Sample output
Please type in string 1: hey
Please type in string 2: bye
The strings are equally long
"""

string_1 = input("Please type in string 1: ")
string_2 = input("Please type in string 2: ")
len_of_str_1 = len(string_1)
len_of_str_2 = len(string_2)

if len_of_str_1 > len_of_str_2:
    print(f"{string_1} is longer")
elif len_of_str_1 < len_of_str_2:
    print(f"{string_2} is longer")
elif len_of_str_1 == len_of_str_2:
    print("The strings are equally long")