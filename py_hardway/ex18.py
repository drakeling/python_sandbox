#Exercise 18

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print_two(arg1, arg2)

def print_one(arg):
    print "arg: %r" % arg

def print_zero():
    print "nil"

print_two("Danke", "Dandy")
print_two_again("Danke", "Dandy")
print_one("FIRST!")
print_zero()
