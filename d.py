#funcion que reciva un map

def insurrectionary(mapped:dict[str, int], key:int) -> bool:
    return mapped.get(key) is not None



def cuenta_letras(palabra : str) -> str:
    dictionary1 = {}
    for letra in palabra:
        if not insurrectionary(dictionary1, letra):
                dictionary1[letra] = 1
        else:
            dictionary1[letra] = dictionary1[letra] + 1
    return dictionary1



print(cuenta_letras("abuela"))
