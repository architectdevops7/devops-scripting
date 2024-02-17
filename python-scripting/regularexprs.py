import re

text = "Hello, my email is architectdevops@email.com"
pattern = r'[\w\.-]+@[\w\.-]+'
matches = re.findall(pattern, text)
print("Email:", matches[0])
