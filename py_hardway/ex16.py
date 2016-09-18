#Exercise 16
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "To exit, hit CTRL-C now, otherwise hit ENTER"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file. Cya!"
#target.truncate()

print "Now let's get three lines from you, the user."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Let's write these lines now."

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print "Closing file and exiting"
target.close()
