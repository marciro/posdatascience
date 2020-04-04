
#Trabalho da aula - Implementar KNN

import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

(X, y) = load_iris(return_X_y=True)


#np.zeros -> Cria uma matriz de zeros
data = train_test_split(X, y, test_size=0.2)# Adicionando o random state para adicionar aleatoriedade na escolha do conjunto de testes
(X_train, X_test, y_train, y_test) = data

#Pegando um ponto para ser a amostra
test = X_test[0,:]

distancias = np.zeros(shape=(len(X_train),1))

labels = np.zeros(shape=len(y_test))

###For calculando as distâncias
for  i in range(len(X_test)):
    distancias = X_test[i] - X_train #Duplica as linhas para adequar o tamanho das matrizes para executar as operações
    distancias = np.square(distancias)
    distancias = np.sum(distancias)

k= 5
#Ordenandos o indices das distancias
indices = np.argsort(distancias)
#Coletando os k menores indices
top_k =indices[:k]
#Recuperando os labels dos k menores
top_k_labels = y_train[top_k]

y_hat = mode(top_k_labels[0][0])
print(top_k_labels)
print(y_hat)
labels[i] = y_hat

#Calculando a acurácia

acertos = np.sum(labels ==y_test)

print(acertos / len(X_test))

