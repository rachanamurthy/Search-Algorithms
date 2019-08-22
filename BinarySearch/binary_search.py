# Implementation of Binary Search Algorithm in Python

def binary_search(array,x):
	if array != []:
		array = sorted(array)
		mid = len(array) / 2
		if array[mid] == x:
			return True
		elif array[mid] > x:
			array = array[0:mid]
			return binary_search(array,x) # <<- need to return it as this is recursive program.
		else:
			array = array[mid+1:len(array)]
			return binary_search(array,x)
	else:
		return False