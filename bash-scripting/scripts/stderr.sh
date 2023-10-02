#!/bin/bash
# Simulate an error
if [ ! -f "non_existent_file.txt" ]; then
    echo "Error: File not found!" >&2
fi
