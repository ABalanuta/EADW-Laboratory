def add_99(x):
	return x + 99




x = 1

print x
x = add_99(x)
print x


print "----"

def somar(x,y = 1):
	return x+y

print somar(2)
print somar(2, 55) 


print "-------------"

function = lambda x, s: x + s**2

print function(2, 4)

