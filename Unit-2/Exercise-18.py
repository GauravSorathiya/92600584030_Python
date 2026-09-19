total = 0

def sum (a,b):
    total = a + b
    print("Inside the function local total : ",total)
    return total

sum(19,21)

print("Outside the function global total : ", total)

