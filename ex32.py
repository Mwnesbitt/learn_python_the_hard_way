the_count = [1,2,3,4]
fruits = ["apples", "organges", "pears", "apricots"]
change = [1,"pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
  print("This is count %d" % number)
  
for fruit in fruits:
  print("The fruit is %s" % fruit)
  
for i in change:
  print("The item is %r" % i)
  
elements = []

for i in range(0,6):
  print("Adding %r to the list" % i)
  elements.append(i)

  
for thing in elements:
  print("Element is %r" % thing)
  
print(elements)

test = range(0,6)
print(test)
for item in test:
  print(item)