list1 = ['Manan','Tanmay','Jaynish']

it = iter(list1)

print(next(it))
print(next(it))
print(next(it),"\n")



dict1 = {
            "Name"   : "Raj",
            "Rollno" : 24,
            "Study"  : "MCA"
        }

for key, values in dict1.items():
    print(f"{key} : {values}")
