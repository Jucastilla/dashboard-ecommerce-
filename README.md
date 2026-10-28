# Análise Exploratória de E-commerce

## Contexto

Este projeto foi desenvolvido durante a formação em **Análise de Dados da EBAC**, utilizando uma base de produtos de e-commerce disponibilizada para a atividade.

A análise foi realizada em **Python**, com **Pandas** para exploração dos dados e cálculo de estatísticas descritivas, além de **Matplotlib** e **Seaborn** para construção das visualizações.

A partir da análise desenvolvida no notebook, o projeto foi ampliado com um dashboard utilizando **Dash e Plotly**, reunindo indicadores, gráficos e resultados em uma aplicação web.

## Objetivo

Explorar os dados de produtos de e-commerce por meio de estatísticas descritivas e visualizações, buscando identificar padrões, distribuições e relações entre as variáveis disponíveis.

Apresentar os indicadores e resultados da análise em um dashboard desenvolvido em Python.

## Desenvolvimento

### Fonte e Exploração dos Dados

Foi utilizado o arquivo `ecommerce_estatistica.csv`, disponibilizado como base para a atividade.

Os dados foram carregados em um DataFrame com **Pandas**. Entre as variáveis exploradas estão:

- Notas dos produtos;
- Preços;
- Descontos;
- Número de avaliações;
- Quantidade vendida;
- Marcas;
- Gênero dos produtos.

Antes da construção dos gráficos, foram calculadas estatísticas descritivas das principais variáveis numéricas para auxiliar na compreensão da distribuição dos dados.

### Análise Exploratória e Visualizações

Foram desenvolvidas sete visualizações utilizando **Matplotlib** e **Seaborn**, cada uma acompanhada de seu objetivo e da interpretação dos resultados:

| Visualização | Objetivo |
|---|---|
| Histograma das notas | Explorar a distribuição das notas dos produtos. |
| Dispersão entre número de avaliações e nota | Investigar a relação entre essas variáveis. |
| Mapa de calor das correlações | Examinar as correlações entre as variáveis numéricas. |
| Gráfico de barras das marcas | Identificar as marcas com maior quantidade de produtos na base. |
| Gráfico de pizza por gênero | Visualizar a participação das categorias de gênero. |
| Gráfico de densidade das notas | Examinar a concentração e a distribuição das notas. |
| Gráfico de regressão entre preço e nota | Investigar a relação linear entre preço e nota. |

### Desenvolvimento do Dashboard

Os indicadores e as visualizações da análise exploratória foram reunidos em um dashboard desenvolvido com **Dash, Plotly, Pandas e NumPy**.

A aplicação apresenta quatro indicadores principais:

- Total de produtos;
- Nota média;
- Preço médio;
- Desconto médio.

As sete visualizações foram recriadas com **Plotly** e organizadas em uma interface web:

- Distribuição das notas dos produtos;
- Relação entre número de avaliações e nota;
- Top 10 marcas com maior quantidade de produtos;
- Distribuição dos produtos por gênero;
- Mapa de calor das correlações;
- Densidade das notas;
- Regressão entre preço e nota.

Também foi adicionada uma seção com os principais resultados identificados durante a análise.

## Resultados

### Notas dos Produtos

As notas apresentaram média de aproximadamente **4,48**, com maior concentração em valores elevados.

### Relação entre Avaliações e Quantidade Vendida

O mapa de calor mostrou uma correlação de **0,91 entre o número de avaliações e a quantidade vendida**, indicando uma forte relação positiva entre essas variáveis no conjunto analisado.

### Relações entre Preço, Nota e Desconto

Foram observadas correlações baixas entre preço, nota e desconto.

O gráfico de regressão entre preço e nota apresentou uma tendência pouco acentuada, indicando baixa relação linear entre essas variáveis. No conjunto analisado, preços mais altos não estiveram necessariamente associados a notas superiores.

### Marcas e Categorias de Gênero

A **Lupo** apresentou a maior quantidade de produtos entre as marcas presentes na base.

As categorias **Masculino** e **Feminino** tiveram maior participação na distribuição dos produtos por gênero, enquanto as demais categorias apresentaram menor representatividade.

### Apresentação dos Resultados

O projeto resultou em um notebook com estatísticas descritivas, sete visualizações e suas interpretações, além de um dashboard com quatro indicadores e os gráficos da análise.

A aplicação web reuniu esses resultados em uma interface organizada para apresentação e exploração dos dados.

## Habilidades Demonstradas

- Análise de dados;
- Python;
- Pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- Plotly;
- Dash;
- Análise exploratória de dados (EDA);
- Estatística descritiva;
- Visualização de dados;
- Análise de correlação;
- Análise de distribuição;
- Regressão linear;
- Desenvolvimento de dashboard;
- DataFrames;
- Interpretação de dados.

## Arquivos do Projeto

Os arquivos estão organizados entre a base de dados, o notebook de análise exploratória e a aplicação do dashboard.

### [Notebook de Análise Exploratória](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/notebooks/analise_exploratoria.ipynb)

Notebook contendo a exploração dos dados, as estatísticas descritivas, as visualizações e a interpretação dos resultados.

### [Aplicação em Dash](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/app.py)

Aplicação desenvolvida em Python com Dash e Plotly, reunindo os principais indicadores, gráficos e resultados da análise exploratória.

### [Base de Dados do Projeto](https://github.com/Jucastilla/dashboard-ecommerce-/blob/main/data/ecommerce_estatistica.csv)

Arquivo `ecommerce_estatistica.csv`, utilizado como fonte de dados para a análise exploratória e o dashboard.
