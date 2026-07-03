# Dashboard para Análise de Dados de E-commerce

Sobre o Projeto

Este projeto foi desenvolvido utilizando Python, Pandas, Plotly e Dash com o objetivo de transformar uma análise exploratória de dados em uma aplicação web interativa.

O trabalho contemplou desde o carregamento e tratamento do conjunto de dados até a construção de um dashboard completo contendo indicadores, gráficos interativos e insights estatísticos para apoio à tomada de decisão.

Etapas Desenvolvidas

1. Carregamento e Preparação dos Dados

Foi realizada a leitura do arquivo ecommerce_estatistica.csv utilizando Pandas para construção do DataFrame principal da aplicação.

Também foram realizadas etapas de preparação dos dados, incluindo:

Leitura do arquivo CSV;
Remoção de colunas desnecessárias;
Organização das variáveis utilizadas na análise;
Centralização do carregamento dos dados para reutilização em toda a aplicação.
2. Construção da Aplicação Web

Foi desenvolvida uma aplicação utilizando Dash, permitindo que o usuário visualize todas as análises diretamente pelo navegador, sem necessidade de executar comandos em Python.

A estrutura da aplicação contempla:

Layout responsivo;
Cards com indicadores principais;
Organização dos gráficos em grade;
Área exclusiva para apresentação dos principais insights obtidos na análise.
3. Indicadores Estatísticos

Foram calculados indicadores descritivos para fornecer uma visão geral do conjunto de dados.

Entre eles:

Total de produtos;
Nota média;
Preço médio;
Desconto médio.

Esses indicadores foram apresentados em formato de cards no topo do dashboard.

4. Visualizações Interativas

Foram desenvolvidos diferentes tipos de gráficos utilizando Plotly.

Histograma

Análise da distribuição das notas dos produtos, incluindo uma linha indicando a média das avaliações.

Gráfico de Dispersão

Relação entre:

Número de avaliações;
Nota dos produtos.

Permitindo identificar possíveis padrões entre popularidade e avaliação.

Gráfico de Barras

Exibição das 10 marcas com maior quantidade de produtos cadastrados.

Gráfico de Pizza

Distribuição percentual dos produtos por gênero.

Foram realizados ajustes na apresentação das categorias para melhorar a legibilidade dos rótulos.

Mapa de Calor

Construção da matriz de correlação entre as variáveis numéricas utilizando Heatmap.

As correlações foram exibidas diretamente sobre o gráfico para facilitar a interpretação.

Curva de Densidade

Representação da distribuição das notas por meio de uma estimativa de densidade.

Regressão Linear

Análise da relação entre:

Preço;
Nota dos produtos.

Incluindo linha de tendência para facilitar a interpretação dos resultados.

5. Geração de Insights

Ao final da aplicação foi desenvolvido um painel contendo os principais insights encontrados durante a análise.

Entre eles:

Quantidade total de produtos analisados;
Nota média dos produtos;
Faixa predominante das avaliações;
Marca com maior quantidade de produtos;
Correlação entre preço e nota;
Correlação entre número de avaliações e quantidade vendida.
6. Organização e Boas Práticas

Durante o desenvolvimento foram aplicadas boas práticas de programação, incluindo:

Separação do código em funções;
Reutilização do DataFrame em toda a aplicação;
Padronização das cores da interface;
Utilização de constantes para configuração visual;
Organização do código em blocos lógicos;
Utilização da biblioteca pathlib para localização segura do arquivo de dados.
Habilidades Demonstradas
Python
Pandas
NumPy
Plotly
Dash
Data Visualization
Exploratory Data Analysis (EDA)
Dashboard Development
Business Intelligence
Data Analytics
Statistical Analysis
Web Application Development
Interactive Visualization

Arquivos do Projeto

📄 app.py — Aplicação principal do Dashboard

📄 ecommerce_estatistica.csv — Base de dados utilizada

📄 requirements.txt — Bibliotecas necessárias para execução do projeto

📄 README.md — Documentação do projeto
