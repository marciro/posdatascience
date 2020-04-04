import numpy as np

# Utilização de funções numéricas em Python

M = np.array([
    #Idade, Altura , Peso
    [10,1.3, 35],
    [34,1.83, 79.7],
    [87,1.6, 69],

])

print(M)
print(M[0,2])
print(M[:,2])
print(M[1:])

print(np.mean(M[:,1]))

peso = M[:,2]
altura = M[:,1]

imc = peso / (altura ** 2)
print(imc)
imc = M[:,2] / np.power(M[:,1],2)
print(imc)

imc = M[:,2] / np.square(M[:,1])
print(imc)

#Máximo das colunas
print (np.max(M, axis=0))
# Máximo das linhas
print(np.max(M,axis=1))
# Média das colunas
print(np.mean(M,axis=0))
# Média das linhas
print(np.mean(M,axis=1))

# Matriz tranposta
print(M.T)


mask  = M[:,0]< 60
print(M[mask,:])