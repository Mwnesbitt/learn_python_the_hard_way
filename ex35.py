from sys import exit

def gold_room():
  print("This room is full of gold.  How much should you take?")
  
  choice = input("> ")
  if "0" in choice or "1" in choice:
    how_much = int(choice)
  else: 
    dead("type a number")
  
  
  if(how_much < 50):
    print("nice, you're not greedy, you win!")
    exit(0)
  else:
    dead("you're too greedy")
    
def bear_room():
  print("There is a bear in here. \nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?")
  bear_moved = False
  while True:
    choice = input("> ")
    if(choice == "take honey"):
      dead("The bear kills you")
    elif(choice == "taunt bear" and not bear_moved):
      print("The bear has moved from the door. YOu can go through it now.")
      bear_moved = True
    elif(choice == "taunt bear" and bear_moved):
      dead("The bear gets pissed and kills you.")
    elif(choice == "open door" and bear_moved):
      gold_room()
    else:
      print("No idea what that means, try something else")



def cthulhu_room():
  print("Flee or eat your head?")
  choice = input("> ")
  if "flee" in choice:
    start()
  elif "head" in choice:
    dead("Well that's that")
  else:
    cthulhu_room()

def dead(why):
  print(why, "Good job")
  exit(0)
  
def start():
  print("You are in a dark room")
  print("There is a door to your right and left")
  print("Which one do you take?")
  choice = input("> ")
  
  if choice == "left":
    bear_room()
  elif choice == "right":
    cthulhu_room()
  else:
    dead("You stumble around the room until you starve.")
    
start()