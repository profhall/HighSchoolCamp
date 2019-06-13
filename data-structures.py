"""
title: data-structures
author: Elizabeth
date: 2019-06-13 11:09
"""

import random

# my_friends = ["Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"]
# print(len(my_friends))
# print(my_friends[3])
# print(my_friends[-1])
# print(my_friends[4:9])
# print(my_friends[-5:])
# print(my_friends[:3])
# print(my_friends[::2])
# my_friends[7] = "Elizabeth"
# print(my_friends)
# my_friends.append("Danny")
# del my_friends[6]
# print(my_friends)





def shake_ball():
    options = ['Yes definitely', 'As I see it, yes', 'Ask again later', 'Cannot predict now', "Don't count on it", "Very doubtful"]
    input("Enter a question: ")
    return random.choice(options)
    # rnd_num = random.randint(0, len(options) - 1)
    # return options[rnd_num]


vowels = ('a', 'e', 'i', 'o', 'u')
print(len(vowels))
print(vowels[1::2])
