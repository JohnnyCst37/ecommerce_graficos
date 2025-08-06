import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('ecommerce_preparados.csv')

# Gráfico de Pizza
#Preparação:
# Criando um dicionário para padronizar os valores
mapeamento_temporadas = {
    'não definido': 'Indefinido',
    'outono/inverno': 'Outono-Inverno',
    'outono-inverno': 'Outono-Inverno',
    'primavera/verão': 'Primavera-Verão',
    'primavera-verão': 'Primavera-Verão',
    'primavera/verão/outono/inverno': 'Todas as Estações',
    'primavera/verão outono/inverno': 'Todas as Estações',
    'primavera-verão outono-inverno': 'Todas as Estações',
    'primavera-verão - outono-inverno': 'Todas as Estações'
}

# Aplicando a substituição
df['Temporada'] = df['Temporada'].replace(mapeamento_temporadas)

# Removendo valores irrelevantes como "2021"
df = df[df['Temporada'] != '2021']

x= df['Temporada'].value_counts().index
y= df['Temporada'].value_counts().values

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title("Distribuição de Vendas por Estação do Ano")
plt.show()
