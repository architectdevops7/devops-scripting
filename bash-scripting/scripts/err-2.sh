#!/bin/bash
# Check if a file exists
if [ ! -f "myfile.txt" ]; then
    echo "Error: File not found!" >&2
    exit 1
fi
