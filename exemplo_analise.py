from collections import defaultdict

import pandas as pd
import numpy as np

def parse_ano(data):
    return int(data.split('/')[-1])


#  Criando um dataframe a partir de um arquivo CSV
df = pd.read_csv('household_power_consumption.txt', delimiter=';', nrows=60000, na_values=['?'])

#df['ano'] = lambda data: int(data.)
df['ano'] = df.Date.apply(parse_ano)
print(df.ano)
print(df.groupby(by='ano').Voltage.mean())
print(df.groupby(by='ano').Voltage.agg({'Voltage': ['mean','max','min','median']}))


print(df.ano.value_counts())

ano_referencia = 2007
#df_anterior = df[df.ano < ano_referencia]
df_anterior = df.query(f'ano < {ano_referencia}')
df_referencia = df.query(f'ano >={ano_referencia}')

print(df_anterior)
print(df_referencia)

media = df_anterior.Voltage.mean()
desvio_padrao = df_anterior.Voltage.std()
print(media, desvio_padrao)

mask = np.abs(df_referencia.Voltage - media) > 2 * desvio_padrao
print(df_referencia[mask])

print (len(df_referencia), len(df_referencia[mask]))

media_anomala = df_referencia[mask].Voltage.mean()
std_anomala = df_referencia[mask].Voltage.std()

print(media, desvio_padrao)
print(media_anomala, std_anomala)