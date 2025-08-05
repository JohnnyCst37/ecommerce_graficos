import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

pd.set_option('display.max_columns', None)

print(df.head())

# histogramas automáticos de todas as colunas numéricas

colunas_numericas = ['Nota', 'N_Avaliações_MinMax', 'Preço_MinMax']

for col in colunas_numericas:
    plt.figure(figsize=(6, 4))
    plt.hist(df[col], bins=20, color='#DF5F2E', edgecolor='black', zorder=2)  # zorder mais alto
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.grid(True, zorder=1)  # zorder mais baixo
    plt.tight_layout()
    plt.show()

    # 'Nota_MinMax', 'N_Avaliações_MinMax', 'Preço_MinMax',
    # 'Qtd_Vendidos_Cod', 'Material_Freq',
    # 'Nota', 'Preço', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Desconto_MinMax', 'Desconto']
   # Agrupamentos
    colunas_numericas = ['Marca_Freq', 'Marca', 'Desconto', 'Nota_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod', 'N_Avaliações_MinMax' ]

    plt.figure(figsize=(12, 8))  # Tamanho total da figura

    # Histograma 1
    plt.subplot(2, 2, 1)
    plt.hist(df[colunas_numericas[0]], bins=20, color='#DF5F2E', edgecolor='black', zorder=2)
    plt.grid(True, zorder=1)
    plt.title(f'Distribuição de {colunas_numericas[0]}')
    plt.xlabel(colunas_numericas[0])
    plt.ylabel('Frequência')

    # Histograma 2
    plt.subplot(2, 2, 2)
    plt.hist(df[colunas_numericas[1]], bins=20, color='#5883a8', edgecolor='black', zorder=2)
    plt.grid(True, zorder=1)
    plt.title(f'Distribuição de {colunas_numericas[1]}')
    plt.xlabel(colunas_numericas[1])
    plt.ylabel('Frequência')

    # Histograma 3
    plt.subplot(2, 2, 3)
    plt.hist(df[colunas_numericas[2]], bins=20, color='#2E8B57', edgecolor='black', zorder=2)
    plt.grid(True, zorder=1)
    plt.title(f'Distribuição de {colunas_numericas[2]}')
    plt.xlabel(colunas_numericas[2])
    plt.ylabel('Frequência')

    # Mapa de Calor da Correlação entre todas
    plt.subplot(2, 2, 4)
    corr = df[colunas_numericas].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlação entre variáveis MinMax')

    plt.tight_layout()
    plt.show()


# Colunas candidatas: Nota, N_Avaliações, Preço,
# Nota_MinMax, N_Avaliações_MinMax, Preço_MinMax
# Marca_Cod, Material_Cod, Temporada_Cod, Qtd_Vendidos_Cod, Marca_Freq, Material_Freq
#
# Faça uma análise detalhada dos dados,
# Descubra quais dados gostaria de destacar e;

# Gráfico de Histograma
# Gráfico de dispersão
# Mapa de calor
# Gráfico de barra
# Gráfico de pizza
# Gráfico de densidade
# Gráfico de Regressão