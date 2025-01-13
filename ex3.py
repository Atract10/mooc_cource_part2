"""
Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

You can assume the number given by the user is always greater than zero.

An example of expected behaviour:

Sample output
Please type in a number: 1.34
Integer part: 1
Decimal part: 0.34
"""

float_number = float(input("Please type in a number: "))
int_part = int(float_number)
dec_part = float_number - int_part
print(f"Integer part:  {int_part}")
print(f"Decimal part: {dec_part}")
