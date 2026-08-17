print('----------------- Mutable (can modify after creation) ----------------')

#set
set1 = set()
set2 = {'James',2,3,'Maths'}

print('Before update : ',set2)
set2.add('Gaurav')

print('Updated set2 : ',set2)

#list
list1 =[1,2,3,4,5,6]

print('\nList1 before delete : ',list1)

del list1[2]
print('After delete list1[2] : ',list1)


#dictionary
dict1 = {"Name":"Gaurav","age":20}

print('\ndictionary : ',dict1)

dict1.update({"City":"Veraval"})
print('After upadated : ',dict1)

print('\n----------------- Immutable (can not be modify after creation) ----------------')

tuple1 = (1,2,3,4,5)

print('Immutable : ',tuple1)

#throws error

tuple1.add(6)
print('Immutable : ',tuple1)


