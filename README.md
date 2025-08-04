![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualização-orange?logo=seaborn)
![License](https://img.shields.io/badge/Licença-MIT-green)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## Sumário

- [Objetivo](#-objetivo)
- [Tecnologias](#-tecnologias-utilizadas)
- [Estrutura](#-estrutura-do-projeto)
- [Exemplos de Gráficos](#-exemplos-de-gráficos)
- [Insights Possíveis](#-insights-possíveis)
- [Como Executar](#-como-executar)
- [Dataset](#-dataset-(recomenda-se-usar-um-ambiente-virtual))
- [Autor](#-autor)
- [Licença](#-licença)


# 📊 Análise Exploratória Gráfica — E-commerce

Este repositório contém um conjunto de gráficos gerados com **Python**, utilizando as bibliotecas `Seaborn`, `Matplotlib` e `Pandas`, para análise exploratória de dados de um dataset de produtos de e-commerce.

## 🎯 Objetivo

Explorar visualmente relações entre variáveis como:

- Preço
- Nota dos produtos
- Número de avaliações
- Frequência por marca e material
- Correlações entre variáveis numéricas

Com o intuito de entender padrões, comportamentos e relações entre atributos do dataset.

---

## 🧰 Tecnologias utilizadas

- Python 3.13
- Pandas
- Matplotlib
- Seaborn
- PyCharm

---

## 📁 Estrutura do Projeto

ecommerce_gráficos/
│
├── sns_gráficos.py # Gráficos com Seaborn
├── plt_gráficos.py # Gráficos com Matplotlib
├── Dash_ecommerce.py # (opcional) versão futura interativa
├── ecommerce_preparados.csv # Dataset tratado
├── plot_types_python/ # Exemplos de tipos de gráficos
└── README.md

yaml
Copiar
Editar

---

## 📊 Exemplos de Gráficos

### ✅ Histograma de Notas dos Produtos
Distribuição das notas atribuídas pelos clientes.

### ✅ Gráfico de Dispersão: Preço vs Nota
Avalia possível correlação entre preço e avaliação dos produtos.

<img src="img/dispersao_nota_preco.png" alt="Dispersão permite analisar tendências" width="600"/>


### ✅ Mapa de Calor
Mostra a correlação entre variáveis numéricas como preço, avaliações e vendas.

<img src="img/mapa_calor.png" alt="Maiores correlações" width="600"/>

### ✅ Gráfico de Barras
Frequência de produtos por marca e por material.

### ✅ Gráfico de Pizza com Agrupamento de “Outros”
Exibe a distribuição de materiais, agrupando os menos frequentes em “Outros”.

<img src="img/Outros_menor_que_5.png" alt="Frequentes vs Raroes" width="600"/>


### ✅ Gráfico de Regressão Linear
Visualiza tendência entre número de avaliações e preço do produto.


## 📌 Insights Possíveis

- Produtos com **mais avaliações tendem a vender mais** (forte correlação).
- **Preço** não tem forte correlação com **nota média**, indicando que produtos baratos podem ser bem avaliados.
- Gráficos ajudam a identificar **marcas dominantes** e **materiais mais populares**.

---

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ecommerce-graficos.git
```

# Dataset (recomenda-se usar um ambiente virtual)
```
pip install pandas matplotlib seaborn
Execute os arquivos .py diretamente no seu IDE (PyCharm ou VSCode)
```


# Autor
Johnny Sorato Martins Fernandes
Consultor de Negócios | Especialista em Dados e Visualização | Diretor Executivo da Tutoreanos - Unidade Primavera do Leste
