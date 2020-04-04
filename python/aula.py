
lista = [2,]*8
print(lista)

tupla =  (1,)*9
print(tupla)

print(tupla is not None)

print(10 in lista)

strings = ['Blumenau', 'Cacau', 'Paulada']
print('au' in strings)

listaRange = list(range(0,10,1))
print(listaRange)

# O set gera um conjunto de objetos únicos a partir de uma lista
# O set
listaRepetidos = [0,2,4,5,7,3,1,3,64,7,8,3,5,1,3,9,5,2,3]
print(listaRepetidos)
print(set(listaRepetidos))

dict_cidades = {'Blumenau':100,'Gaspar':50,'Indaial':30}
print(dict_cidades)

listaEstruturada = ['Blumenau', 300, 'Florianópolis', 350]
listaCidades = listaEstruturada[::2]
listaNumero = listaEstruturada[1::2]
print(listaCidades)
print(listaNumero)

# A partir de uma lista criada com zip ele cria um novo dicionário
print({k:v for (k,v) in zip(listaCidades,listaNumero)})

