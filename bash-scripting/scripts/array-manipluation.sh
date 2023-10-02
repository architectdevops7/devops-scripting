#!/bin/bash

# Declare an array
fruits=("apple" "banana" "cherry")

# Access and manipulate array elements
echo "First fruit: ${fruits[0]}"
fruits[1]="kiwi"
echo "Modified array: ${fruits[@]}"

# Iterate through the array
my_array=("apple" "banana" "cherry")
for item in "${my_array[@]}"; do
    echo "Fruit: $item"
done

# Get the length of an array
array_length=${#my_array[@]}
echo "Array length: $array_length"
