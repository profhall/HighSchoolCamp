"""
title: random_practice
author: Elizabeth
date: 2019-06-12 09:53
"""

import random

name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
print(f"My name is {name} and salary is {salary}")

# rest of work
raise_per = random.randint(0, 100)
raise_amount = salary * raise_per / 100 + salary
print(f"Your raiser is {raise_per}% of ${salary}")
print(f"{name}, your new salary is ${raise_amount}")
