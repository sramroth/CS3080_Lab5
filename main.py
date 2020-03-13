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
		self.i = 0
		self.nbrPrimes = 0
		self.nbrValues = nbrValues

	def __iter__(self):
		return self

	def __next__(self):
		self.i += 1
		if self.nbrPrimes < self.nbrValues:
			while True:
				if IsPrime(self.i):
					self.nbrPrimes += 1
					break
				else:
					self.i += 1
			return self.i
		else:
			raise StopIteration()

def IsPrime(integer):
	if integer > 1:
		for number in range(2, integer):
			if(integer % number) == 0:
				return False
			else:
				continue
		return True

def generator1(n):
	i = 0
	result = -1
	while i < n:
		yield result
		i += 1
		result -= 2

def generator2(n):
	i = 0
	f1 = 1
	f2 = 1
	while i < n:
		yield f1
		temp = f1
		f1 = f2
		f2 = temp + f2
		i += 1

def generator3(n):
	i = 1
	while i <= n:
		yield int((i * (i + 1)) / 2)
		i += 1

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

for i in generator1(nbrValues):
	print(i, end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 4 - Fibonacci Values from a Generator Function
###############################################################
print("\n%-16s" % "Fibonacci: ", end=' ')

for i in generator2(nbrValues):
	print(i, end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 5 - Triangular Values from a Generator Expression
###############################################################
print("\n%-16s" % "Triangular: ", end=' ')

for i in generator3(nbrValues):
	print(i, end=" ")

# Print an end of line character after all of the values
print()

###############################################################
# Exercise 6 - Making Ice Cream with Decorators
###############################################################
print("\n%-16s" % "Ice Cream: ")

# TODO: Make this function a Decorator
def addBrownie(func):
	def wrapper():
		print("Adding Brownie")
		func()
	return wrapper

# TODO: Make this function a Decorator
def addBanana(func):
	def wrapper():
		print("Adding Banana")
		func()
	return wrapper

# TODO: Make this function a Decorator
def addSyrup(func):
	def wrapper():
		func()
		print("Adding Chocolate Syrup")
	return wrapper

# TODO: Make this function a Decorator
def addNuts(func):
	def wrapper():
		print("Adding Nuts")
		func()
	return wrapper

# TODO: Make this function a Decorator
def addCherry(func):
	def wrapper():
		func()
		print("Adding the Cherry on Top!")
	return wrapper

# TODO: Add Decorators to this function
# DO NOT MODIFY ANYTHING BELOW THIS LINE
@addBrownie
@addBanana
@addSyrup
@addNuts
@addCherry
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
