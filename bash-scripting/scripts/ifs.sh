#!/bin/bash

# url="https://www.example.com/path/to/page"
# # Set the IFS to "/"
# IFS="/" read -r -d '' -a url_parts <<< "$url"
# # Access the domain from the array
# domain="${url_parts[2]}"
# echo "Domain: $domain"

config="hostname=localhost port=8080 username=admin"
IFS=" " read -a config_params <<< "$config"
for param in "${config_params[@]}"; do
    key="${param%%=*}"
    value="${param#*=}"
    echo "Key: $key, Value: $value"
done