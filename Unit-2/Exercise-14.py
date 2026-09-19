num = int(input("Enter number to find the sum of digits:"))
sum = 0

while (num>0):
    digit = num % 10 # To get the last digit for adding
    sum += digit 
    num = num // 10 # To remove the last digit

print("Sum of all digits is \t:",sum)
