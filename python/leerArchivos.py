

file = open("file.txt", "w")

for i in range(3):
    file.write("Hello World" + str(i) + "\n")
file.close()


#open file
print("reading file with rread")
file = open("file.txt", "r")
body = file.read()
print(body)
file.close()

print("reading file with for ")
file = open("file.txt", "r")
for line in file:
    print(line, end="")
file.close()

print("read with realine")
file = open("file.txt", "r")
file1 = file.readline()
file2 = file.readline()
file3 = file.readline()
print(file1, end="")
print(file2, end="")
print(file3, end="")
file.close()


#simplificado

with open("file.txt", "w") as file:
    file.write("Hello World")
    file.write("Hello World")
    file.write("Hello World")


with open("file.txt", "r") as file:
    for line in file:
        print(line, end="")


