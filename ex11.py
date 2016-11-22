print("How old are you?  ", end ="")
age = input()
print("How tall are you?  ", end ="")
height = input()
print("How much do you weigh?  ", end="")
weight = input()

print("That makes you %r years old, %r tall, and %r heavy" % (age, height, weight))
"""
using %s would mean that if you type in 4'11" as the height, what gets displayed
has no escape characters, i.e. displayed "nicely" as opposed to literally.  As it is
now, (I think) input() puts in escape characters for special characters, so %r prints
those as you would see them in the code
"""