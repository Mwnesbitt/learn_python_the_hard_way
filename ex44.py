class Parent(object):
  def implicit(self):
    print("Class is PARENT.  Method was \"implicit\"")

class Child(Parent):
  pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit() #this is very cool.  Now I understand what a "base class" means, and why they exist in situations where you need lots of things to do work that changes slightly in each case, but they all do similar style work, like getting information from the same place and posting it to the same place.



class Animal(object):
  def override(self):
    print("Class is Animal.  Method is \"override\"")

class Fish(Parent):
  def override(self):
    print("Class is Fish.  Method is \"override\"")
      
myAnimal = Animal()
myFish = Fish()

myAnimal.override()
myFish.override() #It makes sense for why you need this, but I think before overriding a parent class function you need to really make sure that its necessary, otherwise things can get very complicated.  After all, overriding is why super is necessary at all.


class Meal(object):
  def altered(self):
    print("Class is Meal.  Method is 'altered'")

class Dinner(Meal):
  def altered(self):
    print("Class is Dinner.  Method is 'altered'.  Pre super")
    super(Dinner, self).altered() #so this line calls the "altered" method in the parent class.  since we can't just call our own altered "method" since we overrode it.
    print("Class is Dinner.  Method is 'altered'.  Post super")

myMeal = Meal()
myDinner = Dinner()

myMeal.altered()
myDinner.altered() #Makes sense why this needs to exist, since override exists and you may want access to both an overriden method and the original.  But I can see why it would be good to strucutre things to avoid this if possible, because it could get hairy quickly. 

"""
Note the parts about how in a child __init__ class, you'll also need to call __init__ to grab whatever setup happens in the parent class.
class Child(Parent):
  def __init__(self, stuff):
    self.stuff = stuff
    super(Child, self).__init__()
    