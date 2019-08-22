# Implementation of Linear Search Program
def linear_search(array, x):
  for element in array:
    if element == x:
      return True
  return False