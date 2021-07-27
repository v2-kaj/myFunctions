# This is a function to split characters of a string into elements of a list
# e.g. "Spam" into ['S', 'p', 'a', 'm']

def split(string):
	return list(map(lambda ch:ch+"", string))

#Testing the function

print(split("Spam"))

#Shorter version of the above function; learnt this from a friend :) 

split2 = lambda string:[ch for ch in string]

print(split2("Spam"))
