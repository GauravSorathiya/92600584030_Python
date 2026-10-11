import re

with open("sample.txt","r") as file:
    numbers = re.findall(r"\d+", file.read())

print("Extracted numbers:",numbers)

