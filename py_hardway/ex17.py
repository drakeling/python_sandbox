#Exercise 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

#print "The output fill will be overwritten? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort"
#raw_input()

if exists(to_file):
    print "The output file will be overwritten, hit RETURN to accept"
    raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Copying complete..."
out_file.close()
