import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Gráfico de Histograma, grafico de dispersao,
#  mapa de calor, grafico de bara, grafico de pizza, grafico de densidade e regressao

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.columns)

#vamos criar uma figura com subplots para que os graficos se apresentem de uma vez so
fig, axes = plt.subplots(4, 2, figsize=(15, 20))
fig.tight_layout(pad=10.0, h_pad=10.0, w_pad=10.0)


#grafico de histograma de notas
axes[0, 0].hist(df['Nota'], bins=10, rwidth=0.8)
axes[0, 0].set_title('Frequencia de notas dos produtos')
axes[0, 0].set_xlabel('Nota')
axes[0, 0].set_ylabel('Frequencia')


#grafico de dispersao entre preço e quantidade de itens vendidos
axes[0, 1].scatter(df['Nota'], df['Desconto'])
axes[0, 1].set_title('relaçao entre desconto e nota')
axes[0, 1].set_xlabel('nota')
axes[0, 1].set_ylabel('Desconto')


#mapa de calor
colunas_numericas = ['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod']
corr_matrix = df[colunas_numericas].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('mapa de calor da correlaçao')


#grafico de barra
axes[1, 1].bar(df['Desconto'], df['Nota'])
axes[1, 1].set_title('Nota por Desconto')
axes[1, 1].set_xlabel('Desconto')
axes[1, 1].set_ylabel('Nota')

#grafico de pizza
def categorizar_temporada(temporada):
     if temporada in ['outono/inverno', 'primavera/verão']:
        return temporada
     else:
        return 'Outros'


df['Temporada'] = df['Temporada'].apply(categorizar_temporada)
distribuicao_genero = df['Temporada'].value_counts()
axes[2, 0].pie(distribuicao_genero, labels=distribuicao_genero.index, autopct='%1.1f%%', startangle=90)
axes[2, 0].set_title('distribuicao de produtos por temporada')




#grafico de densidade

sns.kdeplot(df, x='Nota', fill=True, color='green', ax=axes[2, 1])
axes[2, 1].set_title('Grafico de densidade de nota dada aos produtos')
axes[2, 1].set_xlabel('Quantidade da Nota')
axes[2, 1].set_ylabel('Densidade')



#grafico de regressao

sns.regplot(df, x='Preço', y='Nota', color='green', ax=axes[3, 0])
axes[3, 0].set_title('Relacao entre desconto e numero de avaliaçoes')
axes[3, 0].set_xlabel('Preço')
axes[3, 0].set_ylabel('Nota dada ao produto')

fig.delaxes(axes[3, 1])

plt.show()




