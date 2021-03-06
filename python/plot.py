import matplotlib.pyplot as plt
import numpy as np


(fig,ax) = plt.subplots(1,1,figsize= (15,10))

#ax.set_title('Um histograma')
#ax.set_xlabel('Idade')
#ax.set_ylabel('Quantidade')

#Distribuição normal
#idades = np.random.normal(30,5, size=200).astype(int)
#Distribuição exponencial
#idades = np.random.exponential(1, size=200)

#ax.hist(idades)


ax.set_title('Um histograma')
ax.set_xlabel('Desemprego')
ax.set_ylabel('Inflacao')


paises =np.random.choice([0,1,2], size=1000)
desemprego = np.random.normal(10,2, size=1000)
inflacao =  np.random.normal(3,0.1, size=1000)
ax.scatter(desemprego,inflacao)

plt.savefig('./grafico.png')
