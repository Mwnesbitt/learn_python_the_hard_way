from sys import argv

try:
  script,filename = argv

except:
  script = argv
  filename = input("Enter the filename: ")
  

print("We are going to erase %r" % filename)
print("If you don't want to do that, hit CTRL-C (^C)")
print("If you do want that, hit ENTER")

waitup = input("?")

print("Opening the file...")
target = open(filename, 'r+')
#print("I'll show you what's in the file:")
#print(target.read())  #read doesn't work in 'w' mode
print("Truncating the file... goodbye!")
target.truncate() #not necessary in w mode since w mode wipes the file before writing, but r+ mode writes from the beginning and if it doesn't get to the end of the file it leaves it the way it was, thus r+ mode you want to truncate unless you want leftovers from the old file.

print("now I'm going to ask you for 3 lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("now i'll write these back to the file")
target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("And finally, we close the file")
target.close()