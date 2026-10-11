import shutil
import os

shutil.copy("source.txt", "backup.txt")

shutil.move("backup.txt", "folder/backup.txt")

shutil.rmtree("folder")
print("Folder deleted successfully.")
