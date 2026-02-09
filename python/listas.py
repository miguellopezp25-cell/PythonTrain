
lista = [1,2,3,4,5]
listacuadrado = []

for i in lista:
    listacuadrado.append(i**2)

print(listacuadrado)


lista = [1,2,3,4,5]
lista_comprimido = [ i**2 for i in lista if i%2==0]
print(lista_comprimido)
