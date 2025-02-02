"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Sample output
Word: testing

******************************
*          testing           *
******************************
Sample output
Word: python

******************************
*           python           *
******************************
"""
import math

word = input("Word: ")
frame_30 = "*" * 30
frame = "*"
word_len = len(word)
spaces_length = 28 - word_len

print(frame_30)
if (word_len % 2) == 0:
    spaces = " " * math.ceil(spaces_length / 2)
    print(f"{frame}{spaces}{word}{spaces}{frame}")
else:
    spaces_1 = " " * math.ceil(spaces_length / 2)
    spaces_2 = " " * int(spaces_length / 2)
    print(f"{frame}{spaces_1}{word}{spaces_2}{frame}")
print(frame_30)
