# Example of map function
def square(x):
    return x ** 2

# Applying square function to a list of numbers using map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
