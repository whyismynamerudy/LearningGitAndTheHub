import sys
import numpy as np
print(sys.version)

print("Hello World! This is my first Git/GitHub attempt. Wish me luck!")

#lets do something a little more extra

myList = [1, 2, 3, 4, 5]
npMyList = np.array(myList)
print (npMyList**2)

def factorial(x):
	if x == 1:
		return 1

	return (x*factorial(x-1))

number = factorial(5)
print(number)

for i in range(5):
	print("rudy is boss")