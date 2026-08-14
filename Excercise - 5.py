list1 = [37,87,76,88]

print('\n-------- INDEXING ----------')

print('First index number : ',list1[1])
print('Last index number : ',list1[-1])

print('\n-------- SLICING ----------')

print('Second index to last index : ',list1[2:4])

print('\n-------- LIST COMPREHENSIONS ----------')

squares = [x**2 for x in list1]
print('Squares : ',squares)
