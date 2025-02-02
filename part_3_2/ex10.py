"""
Please write a program which asks the user to type in a string. The program then prints out all the substrings which begin with the first character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test
"""

string = input("Please type in a string: ")
str_len = len(string)
index_2 = 1

while index_2 <= str_len:
    print(string[0:index_2])
    index_2 += 1
