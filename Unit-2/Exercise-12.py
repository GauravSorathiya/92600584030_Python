n = int(input('Enter number to check for positive, negative or zero : '))

if n >= 0 :
    if n == 0:
        result = "Zero"
    else :
        result = "Positive"
else :
    result = "Negative"
    
print(f'{n} is {result}.')
