"""
title: string_practice
author: Elizabeth
date: 2019-06-11 13:45
"""

phrase = "here i am!"
slogan = "jskldfjksd"
combined = f"{phrase} {slogan}\n"
print(combined)


def is_letter(character):
    return character[0].lower() in "qwertyuiopasdfghjklzxcvbnm"


print(is_letter("isadfasdf"))
print(is_letter("0"))


def short_hand(short):
    short = short.lower().replace("and", "&").replace("too", "2").replace("you", "U").replace("for", "4")
    short = short.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    return short


print(short_hand("How are you today?"))


def removing(check):
    check = check.lower().replace(" ", "").replace("'", "").replace(",", "").replace("!", "").replace(".", "")\
        .replace(";", "")
    return check


clear = removing("Madam, I'm Adam")
print(clear)


def palindrome(check):
    check = removing(check)
    return check == check[::-1]


print(palindrome("Madam, I'm Adam"))
print(palindrome("Computer"))
