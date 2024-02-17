# Example of reduce function
from functools import reduce

def add(x, y):
    return x + y

# Summing up the elements of a list using reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15
