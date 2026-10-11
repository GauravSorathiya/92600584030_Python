import os
import sys


print("------Using sys module------")

print("Python Version\t: ",sys.version)
print("OS platform\t: ",sys.platform)





print("\n---Directory Operations---")

current_folder = os.getcwd()
print("Current Directory\t: ",current_folder)

os.mkdir("my_folder")
print("Directory 'my_folder' created successfully.")

print("Contents of Current Directory\t: ")
print(os.listdir("."))



print("\n---File Operations---")

file_path = "my_folder/demo.txt"
file = open(file_path,"w")
file.close()

print("File created: ",file_path)

print("Does file exist?:",os.path.exists(file_path))

renamed_path  = "E:/MU/Python/Units Practice/Unit-3/my_folder/sample.txt"
os.rename(file_path, renamed_path)
print("File renamed to:",renamed_path)


os.remove(renamed_path)
print("File deleted successfully.")
os.rmdir("my_folder")
print("Directory 'my_folder' removed successfully.")

