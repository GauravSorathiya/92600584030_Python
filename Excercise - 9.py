print('--- Required arguments ---')

def printme(name,marks):
    "This prints a passed string into this function"
    print("name : ",name)
    print("marks : ",marks)
    return
printme("Gaurav",54)


print('\n--- Keyword arguments ---')
def pet(animal, name):
    print(f"I have a {animal} named {name}.")
pet(name="Sheru",animal="Parrot")


print('\n--- Default arguments ---')
def greet(name, message="Welcome"):
    print(f"Hello {name}! {message}.")
greet("Boby")
greet("Boby","Good Evening")


print('\n--- Variable length arguments ---')
def adder(*num):
    sum=0

    for n in num:
        sum += n

    print("Total is : ",sum)

adder(4,4)
adder(3,5,54,4)
adder(66,55,44,33)
