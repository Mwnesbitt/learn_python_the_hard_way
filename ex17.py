from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Today we'll be coming from %r to %r" %(from_file, to_file))

#in_file = open(from_file)
#indata = in_file.read()

indata = open(from_file).read()

print("the input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready.  Hit ENTER to continue, CTRL-c to abort")
waitup = input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("ok, all done")

out_file.close()
#in_file.close()