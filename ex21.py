def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some maths with just functions!"

age = add(13, 5)
height = subtract(205, 5)
weight = multiply(25, 2)
iq = divide(400, 2)


print "Age: %d, Height: %d, Weight %d, IQ: %d" % (agw, height, weight, iq)


# A puzzle for the extra credit.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand"