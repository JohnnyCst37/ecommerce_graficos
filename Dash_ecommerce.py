# Testando conexão com streamlit para Visualização de Dashboard
# Para visualisar execute python -m streamlit run Dash_ecommerce.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')

# Criando as abas
abas = st.tabs(["Histograma", "Dispersão", "Mapa de Calor", "Pizza", "Regressão"])

# Histograma
with abas[0]:
    st.subheader("Histograma de Nota")
    fig, ax = plt.subplots()
    ax.hist(df['Nota'], bins=20, color='orange', edgecolor='black')
    st.pyplot(fig)

# Dispersão
with abas[1]:
    st.subheader("Dispersão entre Preço e Nota")
    fig, ax = plt.subplots()
    ax.scatter(df['Preço'], df['Nota'], alpha=0.5)
    ax.set_xlabel("Preço")
    ax.set_ylabel("Nota")
    st.pyplot(fig)

# Mapa de Calor
with abas[2]:
    st.subheader("Mapa de Calor das Correlações")
    colunas = ['Nota', 'N_Avaliações', 'Preço']
    corr = df[colunas].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Pizza
with abas[3]:
    st.subheader("Distribuição de Materiais (Pizza)")
    material_counts = df['Material_Cod'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(material_counts, labels=material_counts.index, autopct='%1.1f%%')
    st.pyplot(fig)

# Regressão
with abas[4]:
    st.subheader("Regressão Linear: Preço vs N_Avaliações")
    fig = sns.lmplot(x='Preço', y='N_Avaliações', data=df, height=5, aspect=1.5)
    st.pyplot(fig.figure)
