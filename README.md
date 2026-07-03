# Dashboard Interativo para Análise de Dados de E-commerce

## Sobre o Projeto

Este projeto foi desenvolvido utilizando **Python, Pandas, Plotly e Dash** com o objetivo de transformar uma análise exploratória de dados em uma aplicação web interativa.

O trabalho contemplou desde a leitura do conjunto de dados até a construção de um dashboard responsivo contendo indicadores, gráficos interativos e insights para apoio à tomada de decisão.


## Etapas Desenvolvidas

### 1. Carregamento dos Dados

Foi realizada a leitura do arquivo **ecommerce_estatistica.csv** utilizando **Pandas** para construção do DataFrame principal da aplicação.

As atividades envolveram:

- Leitura do arquivo CSV;
- Estruturação do DataFrame para utilização nas análises;
- Seleção das variáveis utilizadas em cada visualização;
- Cálculo dos indicadores estatísticos utilizados nos cards do dashboard;
- Organização das informações para responder perguntas de negócio por meio de gráficos e métricas.
  

### 2. Análise Exploratória dos Dados

Foi realizada uma análise exploratória com o objetivo de identificar padrões, relações e características relevantes presentes no conjunto de dados.

As análises permitiram responder perguntas de negócio como:

- Como as notas dos produtos estão distribuídas?
- Qual é a relação entre o número de avaliações e a nota dos produtos?
- Quais marcas possuem maior quantidade de produtos cadastrados?
- Como os produtos estão distribuídos por gênero?
- Quais variáveis apresentam maior correlação entre si?
- Existe relação entre o preço e a nota dos produtos?
- Qual é a concentração predominante das avaliações dos produtos?


### 3. Desenvolvimento do Dashboard

Foi desenvolvida uma aplicação utilizando **Dash**, permitindo que todas as análises fossem disponibilizadas em uma interface web interativa.

A aplicação contempla:

- Layout responsivo;
- Cards com indicadores principais;
- Organização dos gráficos em grade;
- Navegação diretamente pelo navegador;
- Seção dedicada aos principais insights encontrados durante a análise.

### 4. Visualizações Interativas

Foram desenvolvidos gráficos utilizando **Plotly** para facilitar a interpretação dos dados.

As visualizações incluem:

- Histograma das notas dos produtos;
- Gráfico de dispersão entre número de avaliações e nota;
- Ranking das 10 marcas com maior quantidade de produtos;
- Distribuição dos produtos por gênero;
- Mapa de calor das correlações;
- Curva de densidade das notas;
- Gráfico de regressão entre preço e nota dos produtos.


### 5. Geração de Insights

Ao final do dashboard foi apresentada uma síntese dos principais resultados obtidos durante a análise.

Entre eles:

- Predominância de produtos voltados ao público masculino;
- Forte correlação entre quantidade vendida e número de avaliações;
- Baixa relação entre preço e nota dos produtos;
- Concentração das avaliações entre aproximadamente 4,2 e 4,9 estrelas;
- Identificação das marcas com maior número de produtos cadastrados.


## Habilidades Demonstradas

- Python
- Pandas
- Plotly
- Dash
- Visualização de Dados
- Análise Exploratória de Dados (EDA)
- Estatística Descritiva
- Desenvolvimento de Dashboards
- Storytelling com Dados
- Business Intelligence
- Manipulação de Dados


## Arquivos do Projeto

## Arquivos do Projeto

- 📄 **[Dashboard em Dash](app.py)**
- 📄 **[Análise Exploratória](tarefa_pratica.ipynb)**
- 📄 **[Base de Dados](ecommerce_estatistica.csv)**
