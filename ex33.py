def my_function(var, increment):
  i=0
  numbers = []
  while i < var:
    print("At the top.  i is %d" %i)
    numbers.append(i)
    i = i + increment
    print("numbers now: ", numbers)
    print("At the bottom.  i is %d" %i)
  return numbers

loop = int(input("What do you want the loop limit to be? :"))
increment = int(input("What do you want the increment to be? :"))
list = my_function(loop, increment)  # kind of a goofy function because it acts like a void function because its primary purpose is printing but also returns the list
  
print("The numbers: ", list)

for num in list:
  print(num)
  
  
for i in range(0, loop, increment):
  print(i)  
