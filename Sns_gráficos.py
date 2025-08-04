import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_preparados.csv')

# 01_FREQUÊNCIA DE NOTAS DOS PRODUTOS
sns.set_style("whitegrid")
sns.histplot(data=df, x='Nota', bins=20, color='#DF5F2E', edgecolor='black')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.title('Distribuição das Notas dos Produtos')
plt.show()

# 02_DISPERSÃO PREÇO E NOTA
sns.set_style("whitegrid") # Estilo similar ao _mpl-gallery
plt.figure(figsize=(8, 5)) # Tamanho da figura
# Gráfico de dispersão com Seaborn
sns.scatterplot(data=df, x='Preço', y='Nota', color='teal', alpha=0.6)
# Título e rótulos
plt.title('Dispersão entre Preço e Nota')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.show()

# 03_MAPA DE CALOR
# Seleção das variáveis normalizadas
# Forte correlação entre N_Avaliações_MinMax e Qtd_Vendidos_Cod
# N_Avaliações_MinMax x Qtd_Vendidos_Cod =	0.90.
# Produtos com mais avaliações quase sempre têm mais vendas.

variaveis_numericas = ['Nota_MinMax', 'N_Avaliações_MinMax', 'Preço_MinMax',
                       'Qtd_Vendidos_Cod', 'Marca_Freq', 'Material_Freq']

# Cálculo da matriz de correlação
df_corr = df[variaveis_numericas].corr()

# Estilo Seaborn
sns.set_style("white")  # ou "whitegrid", "dark", "ticks", "darkgrid"
plt.figure(figsize=(10, 8)) # Tamanho da figura
# Mapa de calor com anotações
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="Oranges", linewidths=0.5, linecolor='white')
plt.title('Mapa de Calor das Correlações entre Variáveis Numéricas')
plt.show()

#  04_MARCA_COD VS QUANTIDADE_ GRAFICO_01_LARANJA
# Devido o excesso de colunas não ficou adequado. Mas Destaca outiliers
# Por isso vamos propor abaixo agrupar fequências menores que 5% e top 20.
# Objetivo: entender se as frequências menores agrupadas tem o mesmo peso que os outiliers.
sns.set_style("whitegrid")
marcas = df['Marca_Cod'].value_counts().reset_index() # Frequência das marcas
marcas.columns = ['Marca_Cod', 'Quantidade']
plt.figure(figsize=(10, 6))
# Gráfico de barras com Seaborn
sns.barplot(data=marcas, x='Marca_Cod', y='Quantidade', color='#DF5F2E', edgecolor='black')
# Título e rótulos
plt.title('Quantidade de Produtos por Marca')
plt.xlabel('Marca (Codificada)')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.show()


# 05_MARCA_COD VS QUANTIDADE_ GRAFICO_TOP 20
# Construído a título de teste, mas ineficaz para a análise.
top_n = 20
marcas = df['Marca_Cod'].value_counts().head(top_n).reset_index()
marcas.columns = ['Marca_Cod', 'Quantidade']

plt.figure(figsize=(10, 8))
sns.set_style("whitegrid")
sns.barplot(data=marcas, y='Marca_Cod', x='Quantidade', color='#DF5F2E')

plt.title(f'Top {top_n} Marcas com Mais Produtos')
plt.xlabel('Quantidade')
plt.ylabel('Marca (Codificada)')
plt.tight_layout()
plt.show()


#  06_MARCA_COD VS QUANTIDADE_ GRAFICO - BARRAS
# Aqui o grafico filtrou automáticamente os 21 mais frequentes.
sns.set_style("whitegrid")

# Frequência dos materiais
materiais = df['Material_Cod'].value_counts().reset_index()
materiais.columns = ['Material_Cod', 'Quantidade']

# Tamanho da figura
plt.figure(figsize=(10, 8))

# Gráfico de barras horizontal
sns.barplot(data=materiais, y='Material_Cod', x='Quantidade', color='#DF5F2E')

# Títulos e rótulos
plt.title('Distribuição de Materiais dos Produtos')
plt.xlabel('Quantidade')
plt.ylabel('Material (Codificado)')
plt.show()

# 07_GRAFICO DE PARETO_ visualmente desagradável para os dados.
materiais = df['Material_Cod'].value_counts().reset_index()
materiais.columns = ['Material_Cod', 'Quantidade']
materiais['Acumulado (%)'] = materiais['Quantidade'].cumsum() / materiais['Quantidade'].sum() * 100

fig, ax1 = plt.subplots(figsize=(12, 6))
# Barras
sns.barplot(data=materiais, x='Material_Cod', y='Quantidade', ax=ax1, color='#DF5F2E')
ax1.set_ylabel('Quantidade')
ax1.set_xlabel('Material (Codificado)')
ax1.tick_params(axis='x', rotation=45)

# Linha acumulada
ax2 = ax1.twinx()
ax2.plot(materiais['Material_Cod'], materiais['Acumulado (%)'], color='black', marker='o')
ax2.set_ylabel('Acumulado (%)')

plt.title('Gráfico de Pareto dos Materiais dos Produtos')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# 08_GRAFICO PIZZA AGRUPANDO OS MÍNIMOS DE 5% (com legenda)
sns.set_style("whitegrid")

# Contagem dos materiais
materiais = df['Material_Cod'].value_counts()
total = materiais.sum()
limite_percentual = 0.05

# Agrupamento
materiais_frequentes = materiais[materiais / total >= limite_percentual]
materiais_outros = materiais[materiais / total < limite_percentual]
materiais_agrupados = materiais_frequentes.copy()
materiais_agrupados['Outros'] = materiais_outros.sum()

# Acessa uma paleta de cores pastel chamada Set3, ótima para diferenciar categorias.
# colors[:len(... Pega apenas a quantidade de cores necessária com base no número de fatias (categorias).
cores = plt.cm.Set3.colors[:len(materiais_agrupados)]

# Gráfico
# wedges: as fatias (os setores desenhados) – usados na legenda.
# texts: os rótulos (se labels fosse usado).
# autotexts: os percentuais desenhados sobre cada fatia (autopct).
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    materiais_agrupados.values,       # Quantidade de cada material
    labels=None,                      # Sem rótulo direto na pizza
    autopct='%1.1f%%',                # Mostra % com 1 casa decimal
    startangle=90,                    # Começa do topo (em vez da direita)
    colors=cores,                     # Paleta definida acima
    wedgeprops={'edgecolor': 'white'}  # Bordas brancas para separar as fatias
)

# Adiciona legenda
plt.legend(
    wedges,                       # As fatias (para associar cor + legenda)
    materiais_agrupados.index,    # Os nomes (ex: Algodão, Poliéster, Outros)
    title="Materiais",            # Título da legenda
    loc="center left",            # Posição relativa da legenda
    bbox_to_anchor=(1, 0.5)       # Posiciona a legenda fora do gráfico, à direita
)


# Título de ajuste
# plt.title(...): define o título acima do gráfico.
# plt.axis('equal'): mantém o círculo perfeito (sem esticar para oval).
# plt.tight_layout(): ajusta os espaços automaticamente para evitar corte de textos.
plt.title('Distribuição de Materiais dos Produtos (com agrupamento de Outros)')
plt.axis('equal')
plt.tight_layout()
plt.show()

# 09_GRAFICO DE DENSIDADE (KDE) – Densidade de Preço
# sns.kdeplot(...) → É a função ideal para gráficos de densidade (KDE).
# fill=True → Preenche a área abaixo da curva, tornando o gráfico mais visual.
# color='purple' → Define uma cor personalizada para a curva.
sns.kdeplot(df['Preço'], fill=True, color='purple')
plt.title('Distribuição de Densidade de Preço')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()


# Gráfico de Regressão (Linear) – Preço vs. N_Avaliações
# (com legenda automática "hue") - inviável devido o número de marcas
sns.set_style("whitegrid")

g = sns.lmplot(
    x='Preço',
    y='N_Avaliações',
    data=df,
    hue='Marca_Cod',  # ou 'Categoria' se tiver
    height=6,
    aspect=1.5,
    scatter_kws={'alpha': 0.4},
    line_kws={'linewidth': 2}
)

# Eixos e título
g.set_axis_labels("Preço", "Número de Avaliações")
g.fig.suptitle('Regressão Linear por Marca', fontsize=14)
g.tight_layout()
g.fig.subplots_adjust(top=0.92)  # espaço para o título

# Legenda já aparece automaticamente
plt.show()


# GRAFICO DE REGRESSÃO (Linear) – Preço vs. N_Avaliações
# com legenda manual

# ANÁLISE DO GRÁFICO:
# Tendência geral:
# A inclinação da linha é positiva, mas suave, ou seja:
# Produtos mais caros tendem a ter um número ligeiramente maior de avaliações — mas a correlação é fraca.
# Dispersão forte:
# Há muitos produtos baratos com milhares de avaliações, e vários caros com poucas.
# Isso indica que outros fatores além do preço influenciam fortemente no número de avaliações:
# Popularidade da marca
# Tempo de exposição no marketplace
# Tipo de produto
# Estratégia de marketing
# Pontos extremos (outliers):
# Alguns produtos abaixo de R$ 100 têm mais de 6000 avaliações.
# Produtos acima de R$ 400, na maioria, não têm avaliações altas.
# Isso pode indicar nichos premium pouco vendidos.

sns.set_style("whitegrid")

# Criar o gráfico
g = sns.lmplot(
    x='Preço',
    y='N_Avaliações',
    data=df,
    height=6,
    aspect=1.5,
    scatter_kws={'alpha': 0.4},
    line_kws={'color': 'red', 'label': 'Regressão Linear'}
)

# Título e rótulos
g.set_axis_labels("Preço", "Número de Avaliações")
g.fig.suptitle('Regressão Linear: Preço vs Número de Avaliações', fontsize=14)
g.tight_layout()
g.fig.subplots_adjust(top=0.92)

# Adicionar legenda manual
plt.legend(loc='upper left')  # precisa ser depois do `plt.show()` para aparecer

plt.show()

# IMPORTANTE
# Quando você usa sns.lmplot(...):
# Ele cria a figura dentro do Seaborn, então o uso de plt.legend() nem sempre funciona diretamente.
# Para adicionar legenda corretamente, você deve trabalhar com o objeto retornado (g) e o eixo dele.
# plt.legend() → funciona com gráficos matplotlib direto.
# sns.lmplot() → é um gráfico Seaborn que exige .ax.legend() para funcionar corretamente.
