idades = [30,24,25,43]

'''Descrição de funções como o Javadoc-  docstring
    quando colocado na primeira linha de uma função
'''

# Exemplos com FOR e WHILE - Laços iterativos #
for idade in idades:
    print(idade)

print(idades)

c = 0
while c < 1000 :
    c+=1
    print(c)

for (i, idade) in enumerate(idades):
    print(i,idade)

for i in range(1000):
    print(i)

for i in range(len(idades)):
    print(i,idades[i])

# Laços com condicionais

for idade in idades:
    if idade > 30 :
        print('Idade maior que 30')
    else:
        print('Idade menor que 30')

idade_pares = []
idade_impares = []
for idade in idades:
    if idade % 2 == 0:
        idade_pares.append(idade)
    else:
        idade_impares.append(idade)

print(idade_pares)
print(idade_impares)

#list-comprehension
idade_pares_quick = [v for v in idades if v%2 == 0]
print(idade_pares_quick)

print(sorted(idade_pares_quick))

for idade in idades:
    if idade % 3 == 0:
        pass
    elif idade % 2 == 0:
        pass
    else:
        ...


