import matplotlib.pyplot as plt
import numpy as np


(fig,ax) = plt.subplots(1,1,figsize= (15,10))

ax.set_title('Um histograma')
ax.set_xlabel('Idade')
ax.set_ylabel('Quantidade')

idades = np.random.normal(30,5, size=200).astype(int)
ax.hist(idades)

plt.savefig('./grafico.png')