"""
Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

Sample output
Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""

number = int(input("Please type in a number: "))
multiplier_num_1 = 1

while multiplier_num_1 <= number:
    multiplier_num_2 = 1
    while multiplier_num_2 <= number:
        print(f"{multiplier_num_1} x {multiplier_num_2} = {multiplier_num_1 * multiplier_num_2}")
        multiplier_num_2 += 1
    multiplier_num_1 += 1
