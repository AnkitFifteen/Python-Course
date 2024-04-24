import os

filePath = "IPYNB/FileOperations/demo.txt"
f = open(filePath, "r")
print(f.read())
print(f.readline())
for i in f:
    print(i)
f.close()

f = open(filePath, "w")
f.write("this is the new content of file. Previous content is now deleted.")
f.close()

f = open(filePath, "a")
f.write("this is the new content of file. Previous content is not deleted.")
f.close()

os.remove(filePath)