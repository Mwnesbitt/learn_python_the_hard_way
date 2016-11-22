def print_two(*args): #I didn't know you could have a *args, i.e. a function that takes an arbitrary number of input params
  arg1, arg2 = args
  print("arg1 is %r and arg2 is %r" % (arg1, arg2))

def print_two_again(arg1, arg2):
  print("arg1 is %r and arg2 is %r" % (arg1, arg2))

def print_all(*args):
  print("I'll print however many args you send me!")
  for arg in args:
    print(arg)

    
print_two("Mark", "Nesbitt")
print_two_again("Mark", "Nesbitt")
print_all("first one", "second one", "third one", "fourth one")