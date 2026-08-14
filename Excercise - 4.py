print("--- 1. STRING SLICING DEMONSTRATION ---")

sample = "Python Programming is fun!"

print(f"\nOriginal String\t\t: ",sample)
print("First 6 character \t: ",sample[0:6])
print("Slice after index 7\t:",sample[7:])
print("up to index 6\t\t: ",sample[:6])
print("Every second characters\t: ",sample[::2])
print("Last 4 characters\t: ",sample[-4:])
print("Reversed string \t:",sample[::-1]);

print("\n--- 2. STRING FORMATTING ---")

name = "Meet"
marks = 98.552

F_string = f"Hello {name}, my marks is {marks:.2f}%."
print("F-string\t:",F_string)

Format = "Hello {}, my marks is {:.2f}%.".format(name,marks)
print(".format\t\t:",Format)

legacy = "Hello %s, my marks is %.2f%%."% (name,marks)
print("% Operator\t:",legacy)

print("\n--- 3. BUILD-IN STRING FUNCTIONS ---")

text = "ArTifIcial IntElliGenCe"

print("\nText change to lower\t: ",text.lower())
print("Text change to upper\t: ",text.upper())
print("Check length of the text: ",len(text))
print("Replace new with text\t: ",text.replace("ArTifIcial","O"))
print("Capitalized\t\t: ",text.capitalize())
print("Title case\t\t: ",text.title())
print("Strip whitespace\t: "," Python   ".strip())
print("Find the position of 'i': ",text.find("i"))
print("Count of the 'i'\t: ",text.count("i"))
print("Split the string\t:",text.split(" "))


