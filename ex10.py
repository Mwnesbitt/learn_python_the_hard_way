tabby_cat = "\tI'm tabbed in."
persion_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\cat." 

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persion_cat)
print(backslash_cat)
print(fat_cat)

for i in ["/", "-", "|", "\\", "|"]:
    print("%s\r" % i)

    
print("test string %r more test" % "\n") #r inserts the variable "pre-operation," i.e. the way you would write it in the code
print("test string %s more test" % "\n") #s inserts the variable having acted on it the way it would be when printed 