# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Modifying values
my_dict['age'] = 35
print("Updated age:", my_dict['age'])

# Adding new key-value pairs
my_dict['gender'] = 'Male'
print("Updated dictionary:", my_dict)

# Removing key-value pairs
removed_value = my_dict.pop('city')
print("Removed value:", removed_value)
print("Dictionary after pop:", my_dict)
