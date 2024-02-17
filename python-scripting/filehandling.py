# Reading from a file
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
