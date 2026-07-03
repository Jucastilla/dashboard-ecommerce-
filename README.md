# Dashboard para Análise de Dados de E-commerce

## Sobre o Projeto

Este projeto foi desenvolvido utilizando Python, Pandas, Plotly e Dash com o objetivo de transformar uma análise exploratória de dados em uma aplicação web interativa.

O trabalho contemplou desde o carregamento e preparação do conjunto de dados até a construção de um dashboard completo contendo indicadores, gráficos interativos e insights estatísticos para apoio à tomada de decisão.

---

## Etapas Desenvolvidas

### 1. Carregamento e Preparação dos Dados

Foi realizada a leitura do arquivo **ecommerce_estatistica.csv** utilizando Pandas para construção do DataFrame principal da aplicação.

Também foram realizadas etapas de preparação dos dados, incluindo:

- Leitura do arquivo CSV;
- Remoção de colunas desnecessárias;
- Organização das variáveis utilizadas na análise;
- Centralização do carregamento dos dados para reutilização em toda a aplicação.

---

### 2. Desenvolvimento da Aplicação Web

Foi desenvolvida uma aplicação utilizando **Dash**, permitindo que o usuário visualize todas as análises diretamente pelo navegador, sem necessidade de executar comandos em Python.

A estrutura da aplicação contempla:

- Layout responsivo;
- Cards com indicadores principais;
- Organização dos gráficos em grade;
- Área exclusiva para apresentação dos principais insights obtidos na análise.

---

### 3. Indicadores Estatísticos

Foram calculados indicadores descritivos para fornecer uma visão geral do conjunto de dados.

Entre eles:

- Total de produtos;
- Nota média;
- Preço médio;
- Desconto médio.

---

### 4. Visualização dos Dados

Foram desenvolvidos diversos gráficos interativos utilizando Plotly para facilitar a análise exploratória.

As visualizações incluem:

- Histograma das notas dos produtos;
- Gráfico de dispersão entre número de avaliações e nota;
- Ranking das 10 marcas com maior quantidade de produtos;
- Distribuição dos produtos por gênero;
- Mapa de calor das correlações;
- Curva de densidade das notas;
- Regressão entre preço e nota dos produtos.

---

### 5. Geração de Insights

Ao final do dashboard foi adicionada uma seção contendo os principais insights obtidos durante a análise.

Entre eles:

- Predominância de produtos do público masculino;
- Forte correlação entre número de avaliações e quantidade vendida;
- Preço com baixa influência sobre a nota dos produtos;
- Concentração das avaliações entre 4,3 e 4,8 estrelas;
- Marcas com maior quantidade de produtos cadastrados.

---

## Habilidades Demonstradas

- Python
- Pandas
- Plotly
- Dash
- Visualização de Dados
- Data Analytics
- Estatística Descritiva
- Análise Exploratória de Dados (EDA)
- Desenvolvimento de Dashboards
- Storytelling com Dados
- Business Intelligence
- Manipulação de Dados

---

## Arquivos do Projeto

📄 Dashboard em Dash (`app.py`)

📄 Base de Dados (`ecommerce_estatistica.csv`)

📄 Notebook de Desenvolvimento (`tarefa_pratica.ipynb`)
