square_list = [x**2 for x in range(1,6)]
print("List Comprehension : ",square_list)

square_dict = {x:x**2 for x in range(1,6)}
print("Dictionary Comprehension : ",square_dict)

square_set = {x**2 for x in range(1,6)}
print("Set Comprehension : ",square_set)

