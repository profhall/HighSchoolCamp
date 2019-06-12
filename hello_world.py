"""
title: hello_world
author: Elizabeth
date: 2019-06-11 10:52
"""

# import random
#
# print(random.choice("hello"))


import random
import math


def dist_form(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))

output = dist_form(x1, y1, x2, y2)
print(output)
#
# def get_raise(name, salary):
#     print(f"My name is {name} and salary is {salary}")
#
#     # rest of work
#     raise_per = random.randint(0, 100)
#     raise_amount = salary * raise_per / 100 + salary
#     print(f"Your raiser is {raise_per}% of ${salary}")
#     print(f"{name}, your new salary is ${raise_amount}")
#
#
# get_raise("bob", 12345)
# print("="*30)
# get_raise("elizabeth", 543)
# print("="*30)
# get_raise("sue", 23)
# print("="*30)
# get_raise("joe", 86)
