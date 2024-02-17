# Example of filter function
def is_even(x):
    return x % 2 == 0

# Filtering even numbers from a list using filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
