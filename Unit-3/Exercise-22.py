a=1212
b=242
print("------- Standard Syntax --------")
import Calc
add = Calc.add(a,b)
print("Addition\t: ",add)

print("\n------- Specific Extraction --------")
from Calc import add,sub
add = Calc.add(a,b)
sub = Calc.sub(a,b)

print("Addition\t: ",add)
print("Subtraction\t: ",sub)

print("\n------- Specific Low-Level --------")
from Calc import *
add =  Calc.add(a,b)
print("Addition\t: ",add)




