"""
title: string_practice
author: Elizabeth
date: 2019-06-11 13:45
"""

favorite_things = """Some of my favorite things are bird watching, jogging,
listening to podcasts, and coding in Python."""

x = favorite_things[3:15:2]

print(x)

my_name = "Emily"
print("E" in my_name or "e" in my_name)
print(len(my_name))

x = my_name.upper()
print(type(x))
print(my_name)

greetings = input("Enter greeting here")
new_greeting = greetings.replace("salve", "")
print(new_greeting)

