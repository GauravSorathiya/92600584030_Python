import re

txt = "My Name is Gaurav Sorathiya."
x = re.search("^My.*Sorathiya$",txt)


if x:
    print("YES! We hava a match.")
else:
    print("No Match")
