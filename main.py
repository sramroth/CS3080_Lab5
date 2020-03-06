class Iterator1():
	def __init__(self, nbrValues):
		self.i = 1
		self.nbrValues = nbrValues

	def __iter__(self):
		return self

	def __next__(self):
		if self.i <= self.nbrValues:
			result = self.i ** 3
			self.i += 1
			return result
		else:
			raise StopIteration()

class Iterator2():
	def __init__(self, nbrValues):
		self.i = 1
		self.nbrValues = nbrValues

	def __iter__(self):
		return self

	def __next__(self):
		if self.i <= self.nbrValues:
			result = self.i
			self.i += 1
			for number in range(2, result // 2):
				if (result % number) != 0:
					return result
		else:
			raise StopIteration()

# Use nbrValues as the number of values to generate for Exercises 1-5
nbrValues = int(input("What is the number of items you want to generate?\n"))

###############################################################
# Exercise 1 - Cubed Values from a Generator Object
###############################################################
print("%-16s" % "Cubes: ", end=' ')

for i in Iterator1(nbrValues):
	print(str(i), end=" ")

print("\n")
		
###############################################################
# Exercise 2 - Prime Values from a Generator Object
###############################################################
print("\n%-16s" % "Primes: ", end=' ')

for i in Iterator2(nbrValues):
	print(str(i), end=" ")

print("\n")
		
###############################################################
# Exercise 3 - Odd Negative Values from a Generator Function
###############################################################
print("\n%-16s" % "Odd Negatives: ", end=' ')

# TODO: put your code here

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 4 - Fibonacci Values from a Generator Function
###############################################################
print("\n%-16s" % "Fibonacci: ", end=' ')

# TODO: put your code here

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 5 - Triangular Values from a Generator Expression
###############################################################
print("\n%-16s" % "Triangular: ", end=' ')

# TODO: put your code here

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 6 - Making Ice Cream with Decorators
###############################################################
print("\n%-16s" % "Ice Cream: ")

# TODO: Make this function a Decorator
def addBrownie(func):
	print("Adding Brownie")

# TODO: Make this function a Decorator
def addBanana(func):
	print("Adding Banana")

# TODO: Make this function a Decorator
def addSyrup(func):
	print("Adding Chocolate Syrup")

# TODO: Make this function a Decorator
def addNuts(func):
	print("Adding Nuts")

# TODO: Make this function a Decorator
def addCherry(func):
	print("Adding the Cherry on Top!")

# TODO: Add Decorators to this function
# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream():
	print("Adding Ice Cream")

addIceCream()

###############################################################
# Exercise 7 - Custom Toppings using Decorators and Arguments
###############################################################
print("\n%-16s" % "Custom Toppings: ")

# TODO: Implement a Decorator to add Base ingredients

# TODO: Implement a Decorator to add Topping ingredients

# TODO: Add Decorators to this function with arguments
# DO NOT MODIFY ANYTHING BELOW THIS LINE
def addIceCream2():
	print("Adding Ice Cream")

addIceCream2()
