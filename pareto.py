# -*- coding: utf-8 -*-
"""pareto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GWlBo77IzzRwOgwcjo24barxGbN0Q_Wd
"""

#Importa as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#Cria o DataFrame com duas colunas inciais
df = pd.DataFrame({'razoes': ['Separação errada', 'Faturamento incorreto', 'Atraso da transportadora',
                              'Pedido errado', 'Atraso na entrega', 'Preço errado',
                              'Produto danificado', 'Outros', 'Total'],
                   'ocorrencias': [45,60,125,30,140,20,65,15,500]})

#Adiciona a coluna de cumulativo
df['cumulativo'] = df['ocorrencias'].cumsum()/df['ocorrencias'].sum()*100

#Coloca em ordem descendente
df = df.sort_values(by='ocorrencias', ascending = False)
df

#Configura o gráfico
fig, ax1 = plt.subplots()
ax1.bar(df['razoes'], df['ocorrencias'], color='C0')
ax1.set_ylabel('Número de Ocorrências', color='C0')
ax1.tick_params(axis='y', colors='C0')
ax1.set_xlabel('Razões')
ax1.set_xticklabels(df['razoes'], rotation=90)
ax2 = ax1.twinx()
ax2.plot(df['razoes'], df['cumulativo'], color='C1', marker='D', ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.tick_params(axis='y', colors='C1')
plt.show