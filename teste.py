import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Gráfico de Histograma, grafico de dispersao,
#  mapa de calor, grafico de bara, grafico de pizza, grafico de densidade e regressao

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.columns)

#grafico de histograma de notas
plt.hist(df['Nota'], bins=10, rwidth=0.8)
plt.title('Frequencia de notas dos produtos')
plt.xlabel('Nota')
plt.ylabel('Frequencia')
plt.show()

#grafico de dispersao entre preço e quantidade de itens vendidos

plt.scatter(df['Nota'], df['Desconto'])
plt.title('relaçao entre desconto e nota')
plt.xlabel('nota')
plt.ylabel('Desconto')
plt.show()

#mapa de calor

colunas_numericas = ['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod']
corr_matrix = df[colunas_numericas].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('mapa de calor da correlaçao')
plt.show()

#grafico de barra

plt.bar(df['Desconto'], df['Nota'])
plt.title('Nota por Desconto')
plt.xlabel('Desconto')
plt.ylabel('Nota')
plt.show()

#grafico de pizza


def categorizar_temporada(temporada):
     if temporada in ['outono/inverno', 'primavera/verão']:
        return temporada
     else:
        return 'Outros'


df['Temporada'] = df['Temporada'].apply(categorizar_temporada)
distribuicao_genero = df['Temporada'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(distribuicao_genero, labels=distribuicao_genero.index, autopct='%1.1f%%', startangle=90)
plt.title('distribuicao de produtos por temporada')
plt.show()



#grafico de densidade

sns.kdeplot(df, x='Nota', fill=True, color='green')
plt.title('Grafico de densidade de nota dada aos produtos')
plt.xlabel('Quantidade da Nota')
plt.ylabel('Densidade')
plt.show()


#grafico de regressao

sns.regplot(df, x='Preço', y='Nota', color='green')
plt.title('Relacao entre desconto e numero de avaliaçoes')
plt.xlabel('Preço')
plt.ylabel('Nota dada ao produto')
plt.show()