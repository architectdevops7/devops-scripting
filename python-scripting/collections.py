# Example of using collections.Counter
from collections import Counter

# Counting occurrences of elements in a list
my_list = ['a', 'b', 'c', 'a', 'b', 'a']
counter = Counter(my_list)
print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
