""""
Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h
"""

string = input("Please type in a string: ")
len_of_str = len(string)
if len_of_str > 0:
    while len_of_str > 0:
        len_of_str -= 1
        print(string[len_of_str])
else:
    print("The input string is empty. There is no first character.")