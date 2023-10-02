#!/bin/bash

# STRING MATCH:
string1="apple"
string2="banana"

if [[ "$string1" == "$string2" ]]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

# STRING INEQUALITY
string1="apple"
string2="apple"

if [[ "$string1" != "$string2" ]]; then
    echo "Strings are not equal."
else
    echo "Strings are equal."
fi