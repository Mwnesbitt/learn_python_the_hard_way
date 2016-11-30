import sys #from sys import argv, stdout, stderr
import codecs
from sys import argv
"""
This isn't working properly, due I think to issues with unicode and how python 3 reads and encodes files.  I'm going to move on rather
than work to figure it out-- if something like this comes up again to trip me up I'll try to figure it out then.

from stackoverflow: http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined#16120218 
"""
if sys.stdout.encoding != 'cp850':
  sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
  sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
"""
end stackoverflow code
"""
script, inputfile = argv

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)
  
def print_a_line(line_number, f):
  #print(line_number, f.readline()) 
  
  f.seek(0)
  i=line_number
  while i >0:
    f.readline()
    i=i-1
  print(f.readline())  
  
current_file = open(inputfile)

###current_file.read()
print("First we'll print the whole file:\n")
###current_file.seek(0)
print(current_file.read())
#print_all(current_file)
print("Now we reset our position in the file back to the beginning.\n")
rewind(current_file)

print("let's print 3 lines:\n")
i=0
while i <=3:
  print_a_line(i, current_file)
  i+=1