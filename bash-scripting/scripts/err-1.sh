#!/bin/bash
# Enable exit on error
set -e
# Simulate a command that fails
ls /sbsbs
# This script will exit immediately due to set -e
echo "This line will not be executed."
