"""
Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test
"""

string = input("Please type in a string: ")
str_len = len(string)
index_2 = str_len - 1

while index_2 >= 0:
    print(string[index_2:str_len])
    index_2 -= 1
