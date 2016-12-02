print("You enter a room with two doors.  Do you go through door 1 or door 2?")

door = input("Enter a 1 or a 2: ")

if(door == "1"): #you could use int(door) and get rid of the quotes around 1 because door wouldn't be a string anymore
  print("There's a giant bear here eating cake.  What do you do?")
  print("1. Take the cake")
  print("2. Scream at the bear")
  bear = input("Enter a 1 or a 2: ")
  
  if(bear == "1"):
    print("The bear eats your face.  Good job.")
  elif(bear == "2"):
    print("The bear mauls you.  Good job.")
  else:
    print("Well, doing %s or anything else is probably better.  Bear runs off." % bear)

elif(door == "2"):
  print("Now you're past door 2.  Trippy options are:")
  print("1. Blueberries")
  print("2. Yellow Jackets")
  print("3. Songs")
  insanity = input("Enter 1, 2, or 3")
  
  if(insanity == "1" or insanity == "2"):
    print("you survive")
  elif(insanity == "3"):
    print("you die")
  else:
    print("you have to choose 1 2 or 3.  You broke the program.")

else:
  print("you sit and rot in the room forever.  nice work.") 
  
