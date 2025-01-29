"""
Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

Sample output
Upper limit: 5
1
2
3
4

Please don't use the value True as the condition of your while loop in this exercise!
"""

number = int(input("Upper limit: "))
decreasing_num = number
count_num = 0

while decreasing_num > 0:
    decreasing_num -= 1
    count_num += 1
    if count_num != number:
        print(count_num)