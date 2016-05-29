# This ia a string "", but in this case a "format-string", this string can store a variable in it and print it, save it and send it to a web-server, it can do all sorts of things.
my_name = 'IniOluwa C. Fageyinbo'
my_age = 18
my_height = 200 # inches(LOL!)
my_weight = 50 # lbs(LOL!)
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that really light"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# This line is kinda tricky, but i will get it right
print "If i add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)