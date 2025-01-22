"""
Please write a program which asks the user for a year, and prints out the next leap year.

Sample output
Year: 2023
The next leap year after 2023 is 2024

If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

Sample output
Year: 2024
The next leap year after 2024 is 2028
"""

year = int(input("Year: "))
leap_validation = False
next_leap_year = year + 1
next_leap_year_validation = False
while next_leap_year_validation == False:
    if (next_leap_year % 4 == 0 and next_leap_year % 100 != 0) or (
        next_leap_year % 100 == 0 and next_leap_year % 400 == 0
    ):
        next_leap_year_validation = True
    else:
        next_leap_year += 1


print(f"The next leap year after {year} is {next_leap_year}")
