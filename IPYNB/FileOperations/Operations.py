f = open("demo.txt", "r")
print(f.read())
print(f.readline())
for i in f:
    print(i)
f.close()

f = open("demo.txt", "w")