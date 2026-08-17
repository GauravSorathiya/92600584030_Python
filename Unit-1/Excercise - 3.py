a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = True
d = False

print("=============================")
print("         Arithmetic Operator         ")
print("=============================")

print(f"Addintion \t\t: ",a+b)
print(f"Subtraction \t: ",a-b)
print(f"Multiplication \t: ",a*b)
print(f"Division  \t\t: ",a/b)
print(f"Module of \t\t: ",a%b)

print("=============================")
print("  Relational(Comparison) Operator  ")
print("=============================")

print(f"{a} Greater Than {b}\t: ",a>b)
print(f"{a} Less Than {b}\t: ",a<b)
print(f"{a} Equal To {b}\t: ",a==b)
print(f"{a} Not Equal To {b}\t: ",a!=b)
print(f"{a} Greater Than Equal To {b}\t: ",a>=b)
print(f"{a} Less Than Equal To {b}\t: ",a<=b)

print("=============================")
print("            Logical Operator            ")
print("=============================")

print(f"({a} > {b}) and {c}\t: ", (a > b) and c)
print(f"({a} > {b}) or {c}\t: ", (a < b) or d)
print(f"not {c}\t: ", (not c))
