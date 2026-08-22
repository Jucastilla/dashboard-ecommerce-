# Análise Exploratória de E-commerce

## Sobre o Projeto

Este projeto foi desenvolvido durante a formação em **Análise de Dados da EBAC**, com o objetivo de realizar uma análise exploratória de dados de produtos de e-commerce por meio de diferentes técnicas de visualização.

A análise foi desenvolvida em Python utilizando **Pandas, Matplotlib e Seaborn**, permitindo explorar distribuições, relações entre variáveis, correlações e características presentes no conjunto de dados.

A partir da análise desenvolvida no notebook, o projeto também foi ampliado com a construção de um dashboard utilizando **Dash e Plotly**, reunindo os principais indicadores, visualizações e resultados em uma aplicação web.

## Objetivo

Explorar os dados de produtos de e-commerce por meio de estatísticas descritivas e diferentes tipos de visualização, buscando identificar padrões, distribuições e relações entre as variáveis disponíveis.

O projeto também busca apresentar os resultados de forma visual e organizada por meio de um dashboard desenvolvido em Python.

## Etapas Desenvolvidas

### 1. Fonte e Exploração dos Dados

Para o desenvolvimento do projeto, foi utilizado o arquivo `ecommerce_estatistica.csv`, disponibilizado como base para a atividade.

Os dados foram carregados em um DataFrame utilizando **Pandas** e utilizados ao longo das diferentes etapas da análise.

Entre as variáveis exploradas estão informações relacionadas a:

- Notas dos produtos;
- Preços;
- Descontos;
- Número de avaliações;
- Quantidade vendida;
- Marcas;
- Gênero dos produtos.

Antes da construção das visualizações, foram calculadas estatísticas descritivas das principais variáveis numéricas para auxiliar na compreensão da distribuição dos dados.

### 2. Análise Exploratória dos Dados

A análise exploratória foi realizada em Python utilizando **Pandas, Matplotlib e Seaborn**.

Foram desenvolvidas sete visualizações para investigar diferentes características do conjunto de dados:

- Histograma das notas dos produtos;
- Gráfico de dispersão entre número de avaliações e nota;
- Mapa de calor das correlações;
- Gráfico de barras das marcas com maior quantidade de produtos;
- Gráfico de pizza da distribuição dos produtos por gênero;
- Gráfico de densidade das notas;
- Gráfico de regressão entre preço e nota.

Cada visualização foi acompanhada de seu objetivo e da interpretação dos resultados encontrados.

### 3. Análise dos Resultados

A exploração dos dados permitiu identificar diferentes características do conjunto analisado.

As notas dos produtos apresentaram média de aproximadamente **4,48**, com maior concentração das avaliações em valores elevados.

O mapa de calor mostrou uma correlação de **0,91 entre o número de avaliações e a quantidade vendida**, indicando uma forte relação entre essas duas variáveis.

Por outro lado, foram observadas correlações baixas entre preço, nota e desconto. A análise de regressão entre preço e nota também apresentou uma tendência pouco acentuada, indicando baixa relação linear entre essas variáveis.

Na análise das marcas, a **Lupo** apresentou a maior quantidade de produtos entre as marcas presentes no conjunto de dados.

A distribuição por gênero mostrou maior participação das categorias **Masculino** e **Feminino**, enquanto as demais categorias apresentaram menor representatividade.

### 4. Desenvolvimento do Dashboard

Após a análise exploratória, os resultados foram utilizados na construção de um dashboard desenvolvido em Python com **Dash, Plotly, Pandas e NumPy**.

O dashboard reúne quatro indicadores principais:

- Total de produtos;
- Nota média;
- Preço médio;
- Desconto médio.

As visualizações da análise exploratória também foram recriadas utilizando Plotly e organizadas em uma interface web.

O dashboard apresenta:

- Distribuição das notas dos produtos;
- Relação entre número de avaliações e nota;
- Top 10 marcas com maior quantidade de produtos;
- Distribuição dos produtos por gênero;
- Mapa de calor das correlações;
- Densidade das notas;
- Regressão entre preço e nota.

Também foi adicionada uma seção dedicada aos principais resultados identificados durante a análise.

### 5. Conclusões

A análise exploratória permitiu compreender características importantes dos produtos presentes no conjunto de dados.

As visualizações mostraram uma concentração das avaliações em notas elevadas e uma forte relação entre o número de avaliações e a quantidade vendida.

Em contrapartida, o preço apresentou baixa relação com as notas dos produtos, indicando que produtos de maior valor não necessariamente apresentam avaliações superiores.

Também foi possível identificar as marcas com maior presença no conjunto de dados e analisar a distribuição dos produtos entre diferentes categorias de gênero.

A construção do dashboard permitiu reunir os indicadores e visualizações desenvolvidos durante a análise em uma aplicação web, facilitando a apresentação e exploração dos resultados.

## Habilidades Demonstradas

- Análise de Dados
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Dash
- Análise Exploratória de Dados (EDA)
- Estatística Descritiva
- Visualização de Dados
- Análise de Correlação
- Análise de Distribuição
- Regressão Linear
- Desenvolvimento de Dashboard
- DataFrames
- Interpretação de Dados

## Arquivos do Projeto

Os arquivos do projeto estão organizados entre a base utilizada, o notebook de análise exploratória e a aplicação desenvolvida para apresentação das visualizações.

### Notebook

📓 [Análise Exploratória de Dados](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/notebooks/analise_exploratoria.ipynb)

Notebook contendo a exploração dos dados, estatísticas descritivas, desenvolvimento das visualizações e interpretação dos resultados.

### Dashboard

🐍 [Aplicação em Dash](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/app.py)

Aplicação desenvolvida em Python com Dash e Plotly, reunindo os principais indicadores, gráficos e resultados da análise exploratória.

### Dados

📊 [Base de Dados do Projeto](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/data/ecommerce_estatistica.csv)

Arquivo `ecommerce_estatistica.csv` utilizado como fonte de dados para o desenvolvimento da análise exploratória e do dashboard.
