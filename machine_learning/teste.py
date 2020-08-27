import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_insurance = pd.read_csv('insurance.csv', sep=',', decimal='.')

#Primeiras linhas da tabela
print(df_insurance.head())

# informações do conjunto de dados
df_insurance.info()

#Descrição estatística dos dados
print(df_insurance.describe())



plt.boxplot(df_insurance.age)