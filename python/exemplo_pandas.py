import pandas as pd

# Criando um dataframe a partir de um arquivo CSV
df = pd.read_csv('household_power_consumption.txt', delimiter=';', nrows=10000, na_values=['?'])

print(df)
print(df['Date'])
print(df.Date)
print(df.Date[0])
print(df.Voltage)
print(df.Voltage.mean())#Média
print(df.Voltage.std())
print(df.info())
print(df.describe())