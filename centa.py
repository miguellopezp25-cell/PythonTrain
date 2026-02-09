
def sumaDiccionario(dictionary1: dict[str, int], dictionay2: dict[str,int])-> dict[str,int]:
    diccionario = {}
    for letra, valor in dictionary1.items():
        diccionario[letra] = valor + dictionay2[letra]

    return diccionario

dictionarys = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

dictionarys2 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
print(sumaDiccionario(dictionarys, dictionarys2))



