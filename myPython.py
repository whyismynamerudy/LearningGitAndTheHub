import sys
import numpy as np
print(sys.version)

#print("Hello World! This is my first Git/GitHub attempt. Wish me luck!")

#lets do something a little more extra

#myList = [1, 2, 3, 4, 5]
#npMyList = np.array(myList)
#print (npMyList**2)

class NumberOperations:
	def __init__(self, name):
		self.name = name

	def factorial(self, num):
		if num <= 1:
			return 1

		return (num*self.factorial(num-1))

	def printMyNum(self, num):

		if num == 1:
			print(num)
			return(num)

		printMyNum(self.num-1)
		print(num)


	def fibonacci(self, num):
		if num==1:
			return(0)
		if num==2:
			return(1)

		return(self.fibonacci(num-1)+self.fibonacci(num-2))

	def power(self, num, expo):
		if expo==0:
			return 1

		return (num*self.power(num, expo-1))

	def iterativePower(self, num, expo):
		n=expo
		multi=num
		total=1

		while(n>0):
			total = total*multi
			n-=1

		return total


	def bubbleSort(self, arr): 
	    n = len(arr) 
	  
	    # Traverse through all array elements 
	    for i in range(n): 
	  
	        # Last i elements are already in place 
	        for j in range(0, n-i-1): 
	  
	            # traverse the array from 0 to n-i-1 
	            # Swap if the element found is greater 
	            # than the next element 
	            if arr[j] > arr[j+1] : 
	                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 

myNum = NumberOperations("Bobby")
print(myNum.name)
print(myNum.factorial(5))
print(myNum.power(5, 2))
print(myNum.iterativePower(5, 2))

print(arr)
myNum.bubbleSort(arr)
print(arr)