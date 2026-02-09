


def writeFile():
# crear archivo
    with open("file1.txt", "w") as file:
# escribe 5 trextos
      for i in range(5):
        file.write(f"aeiouaeiouaeiou{i}\n")


def remplaceWorld(word:str) -> str:
    newWord = ""
    for letter in word:
        if letter in "aeiou1234567890":
            newWord += "x"
        else:
            newWord += letter
    return newWord



def readfile():
    #leer y escribir el archovo
    with open("file1.txt","r") as file:
    #leer el archivo
     for line in file:
        cleanLine = line.strip()
        newWords = remplaceWorld(cleanLine)
        print(newWords)


writeFile()
readfile()
