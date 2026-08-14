print('---------------- TUPLE -----------------')
tuple1 = (22,33,44,55)
tuple2 = ('Maths','Chemistry', 'Python')
tuple3 = "a","b","c","d"

print('tuple1[0] : ', tuple1[0])
print('tuple1[1:5] : ', tuple1[1:5])
print('tuple2[2] : ',tuple2[2] )

# following action is not valid for tuples, it will give error(adding new element in tuple)
# tuple1[0] = 100

# combine two tuples
tuple4 = tuple1 + tuple2
print('Concatenation (addition): ',tuple4)

del tuple4;  # after this tuple4 does not exist any more. its generate error

length = len(tuple1)
print('Length of the tuple1 : ',length)

print('Print the repetition of tuple2[2] : ',(tuple2[2])*2)
print('Is that "e" is in tuple3 : ',"e" in tuple3)   

print('Iteration : ')
for x in (1,23,4,5,7,5) : print(x, end = "-")

print('\n\n---------------- SET -----------------')

set1  = {1,2,3,4,6,7}
print('set1 : ',set1)
set1.add(5)
print('set1 after added 5 : ',set1)

set1.discard(3)
print('set1 after discard 3 : ',set1)
