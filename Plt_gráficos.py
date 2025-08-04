import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_preparados.csv')

pd.set_option('display.max_columns', None)

print(df.head())

# histogramas automáticos de todas as colunas numéricas

colunas_numericas = ['Nota', 'N_Avaliações', 'Preço',
                     'Nota_MinMax', 'N_Avaliações_MinMax', 'Preço_MinMax']

for col in colunas_numericas:
    plt.figure(figsize=(6, 4))
    plt.hist(df[col], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribuição de {col}')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.grid(True)
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