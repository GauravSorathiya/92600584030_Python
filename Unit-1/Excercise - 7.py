print('----------------- DICTIONARY ------------------')
dict1  = {1:"first name", 3:"last name","age":33}

# display by specific key
print('a[1] of dict1 : ',dict1[1])
print('a["age"] of dict1 : ',dict1["age"])

# update
dict1.update({"City":"Veraval","Education":"MCA"})
print('updated dict1 : ',dict1)

# pop
dict1.pop(3)
print('Deleted dict1 : ', dict1)

print('\n----------------- ITERATE (loop) ------------------')

for key, value in dict1.items():
    print(f"{key}: {value}")
