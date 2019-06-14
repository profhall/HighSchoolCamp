"""
title: conditionals
author: Elizabeth
date: 2019-06-14 09:40
"""

secret_num = 101
guess = int(input("Enter a secret number: "))
if guess == secret_num:
    print("Yay! You won!")
elif guess > 100:
    print("You're crazy")
elif guess < 0:
    print("WAaaaaay too low")
else:
    print("Loser")
