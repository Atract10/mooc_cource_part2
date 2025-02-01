"""
Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""

string = input("Please type in a string: ")
snd_char = string[1]
snd_to_last_char = string[-2]

if snd_char != snd_to_last_char:
    print("The second and the second to last characters are different")
elif snd_char == snd_to_last_char:
    print(f"The second and the second to last characters are {snd_char}")
