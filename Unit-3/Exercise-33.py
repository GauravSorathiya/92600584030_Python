import math

numbers = [-12,-34,3,9,0,-22]

smallest = min(numbers)
largest = max(numbers)
absolute_val = abs(smallest)
power = pow(absolute_val,2)

print(f"Original numbers\t\t: {numbers}")
print(f"Smallest number\t\t\t: {smallest}")
print(f"Largest number\t\t\t: {largest}")
print(f"Absolute value of {smallest} (abs)\t: {absolute_val}")
print(f"{absolute_val} raised to the power of 2 (pow):{power}")
