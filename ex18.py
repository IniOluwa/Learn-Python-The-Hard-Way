#This is like scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)


#That *args is pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)


#This just takes one arguement
def print_one(arg1):
	print "arg1: %r" % arg1


#This takes no arguements
def print_none():
	print "I got nothing'."


print_two("Ini", "Oluwa")
print_two_again("Ini", "Oluwa")
print_one("First!")
print_none()