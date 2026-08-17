Integer = 20
String = 'Gaurav'
Float = 43.4
Boolean = bool(10 > 9)

print("Integer : ",Integer)
print("String : ", String)
print("Float : ", Float)
print("Boolean  : ", Boolean)

print("\nImplicit Cating : ")
result = Integer + Float
print("Automatic get float : ",result)
print("Data type : ", type(result))

print("\nExplicit Casting : ")
tcfloat = int(Float)
print("\ntype casting.",tcfloat)
print("Data type : ", type(tcfloat))

