from sys import argv

try:
  script,filename = argv

except:
  script = argv
  filename = input("Enter the filename: ")
"""
if(len(argv == 2)):
  script, filename = argv
elif(len(argv==1)):
  script = argv
  filename = input("Enter the filename: ")
else:
  print("Run this by calling the script name and the filename you want to read (optional to call the filename)")
  sys.exit()
"""
#script, filename = argv

txt = open(filename)
print("The file you selected is called %r" % filename)
print(txt.read())
txt.close()


