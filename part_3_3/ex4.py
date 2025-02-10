"""
Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

Sample output
Please type in a number: 5
2
1
4
3
5

Sample output
Please type in a number: 6
2
1
4
3
6
5
"""

number = int(input("Please type in a number: "))
counter_1 = 1
counter_2 = 0

if number > 1:
    while True:
        counter_1 += 1
        counter_2 += 1
        if (counter_1 % 2) == 0:
            print(counter_1)
        if (counter_2 % 2) != 0:
            print(counter_2)
        if counter_1 == number and (number % 2) != 0:
            counter_2 += 1
            print(counter_2)
            break
        elif counter_1 == number and (number % 2) == 0:
            break
else:
    print(number)
