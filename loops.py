"""
title: loops
author: Elizabeth
date: 2019-06-13 13:22
"""

# for i in [89, 41, 73, 90]:
#     print(i, end=" ")
#
# print()
# print("=" * 30)
#
# for i in range(5, 15):
#     print(i, end=" ")
#
# print()
# print("=" * 30)
#
# for i in range(100, 201, 10):
#     print(i, end=" ")
#
# print()
# print("=" * 30)
#
# for i in range(80, 31, -8):
#     print(i, end=" ")
#
# print()
# print("=" * 30)
#
# for i in range(3):
#     print("Alright", end=" ")
#
# print()
# print("=" * 30)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_numbers = 0
# odd_numbers = 0

# temperature = 115
# while temperature > 112:
#     print(temperature, end="-")
#     temperature -= 1  # temperature = temperature - 1
#
# print('The tea is cool enough')
#
# # ====================================
# x_input = input("Enter the x key: ")
#
# while x_input != "x":
#     print("Waiting")
#     x_input = input("Enter the x key: ")
#
# print("Thank you for typing x!")

# num = 10
# while num >= 1:
#     print(num)
#     num -= 1


# x_input = int(input("Enter a number greater than 0: "))
#
# while x_input < 0:
#     x_input = int(input("Enter a number greater than 0: "))
#
# print("Thank you for typing x!")
#
# first = int(input("Enter a number: "))
# second = int(input("Enter a second number: "))
#
# while second < first:
#     second = int(input("Invalid response. Enter a second number: "))
#
# while first <= second:
#     print(first)
#     first += 1


x = input("Enter response ('Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'): ")

# while x != 'Y' or x != 'y' or x != 'yes' or x != 'YES' or x != 'N' or x != 'n' or x != 'no' or x != 'NO':

while x not in ['Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO']:
    x = input("Enter response ('Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'): ")

