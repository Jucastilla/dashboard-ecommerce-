from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

# ======================================================
# 1. CONFIGURAÇÕES GERAIS
# ======================================================

COR_PRINCIPAL = "#2F80ED"
COR_SECUNDARIA = "#56CCF2"
COR_DESTAQUE = "#EB5757"
COR_TEXTO = "#1F2937"
COR_FUNDO = "#F5F7FB"
COR_CARD = "#FFFFFF"

CAMINHO_ARQUIVO = Path(__file__).parent / "data" / "ecommerce_estatistica.csv"

# ======================================================
# 2. CARREGAMENTO DOS DADOS
# ======================================================

# O DataFrame é carregado uma única vez e usado em todos os gráficos.
df = pd.read_csv(CAMINHO_ARQUIVO)

# Remove coluna automática de índice, caso exista.
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# ======================================================
# 3. FUNÇÕES PARA CRIAÇÃO DOS GRÁFICOS
# ======================================================


def criar_histograma():
    media_nota = df["Nota"].mean()

    fig = px.histogram(
        df,
        x="Nota",
        nbins=20,
        title="Distribuição das Notas dos Produtos",
        labels={"Nota": "Nota do Produto", "count": "Quantidade"},
        color_discrete_sequence=[COR_PRINCIPAL]
    )

    fig.add_vline(
        x=media_nota,
        line_dash="dash",
        line_color=COR_DESTAQUE,
        annotation_text=f"Média: {media_nota:.2f}",
        annotation_position="top left"
    )

    fig.update_layout(
        xaxis_title="Nota do Produto",
        yaxis_title="Quantidade de Produtos",
        template="plotly_white"
    )

    return fig


def criar_dispersao():
    fig = px.scatter(
        df,
        x="N_Avaliações",
        y="Nota",
        title="Relação entre Número de Avaliações e Nota",
        labels={
            "N_Avaliações": "Número de Avaliações",
            "Nota": "Nota do Produto"
        },
        color_discrete_sequence=[COR_PRINCIPAL],
        hover_data=["Título", "Marca", "Preço"]
    )

    fig.update_traces(marker=dict(size=9, opacity=0.65))
    fig.update_layout(template="plotly_white")

    return fig


def criar_mapa_calor():
    colunas = ["Nota", "N_Avaliações", "Preço", "Desconto", "Qtd_Vendidos_Cod"]
    correlacao = df[colunas].corr()

    fig = go.Figure(
        data=go.Heatmap(
            z=correlacao.values,
            x=correlacao.columns,
            y=correlacao.columns,
            colorscale="RdBu",
            zmin=-1,
            zmax=1,
            text=np.round(correlacao.values, 2),
            texttemplate="%{text}",
            textfont={"size": 12},
            colorbar=dict(title="Correlação")
        )
    )

    fig.update_layout(
        title="Mapa de Calor das Correlações",
        template="plotly_white"
    )

    return fig


def criar_barras():
    top_marcas = df["Marca"].value_counts().head(10).reset_index()
    top_marcas.columns = ["Marca", "Quantidade"]

    fig = px.bar(
        top_marcas,
        x="Marca",
        y="Quantidade",
        text="Quantidade",
        title="Top 10 Marcas com Maior Quantidade de Produtos",
        labels={"Marca": "Marca", "Quantidade": "Quantidade de Produtos"},
        color_discrete_sequence=[COR_PRINCIPAL]
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(template="plotly_white")

    return fig


def criar_pizza():
    genero = df["Gênero"].value_counts()
    top5 = genero.head(5).copy()
    top5["Outros"] = genero.iloc[5:].sum()

    fig = px.pie(
        names=top5.index,
        values=top5.values,
        title="Distribuição dos Produtos por Gênero",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_traces(
        textposition="outside",
        textinfo="percent+label",
        pull=[0.02, 0.02, 0.03, 0.05, 0.06, 0.06],
        marker=dict(line=dict(color="white", width=2))
    )

    fig.update_layout(
        template="plotly_white",
        uniformtext_minsize=11,
        uniformtext_mode="hide",
        legend=dict(
            orientation="v",
            y=0.5,
            x=1.02
        ),
        margin=dict(t=70, b=70, l=40, r=40)
    )

    return fig


def criar_densidade():
    notas = df["Nota"].dropna().values
    eixo_x = np.linspace(notas.min(), notas.max(), 200)

    # Cálculo simples de densidade sem depender de bibliotecas extras.
    desvio = notas.std()
    n = len(notas)
    largura_banda = 1.06 * desvio * (n ** (-1 / 5))

    densidade = np.zeros_like(eixo_x)
    for nota in notas:
        densidade += np.exp(-0.5 * ((eixo_x - nota) / largura_banda) ** 2)

    densidade = densidade / (n * largura_banda * np.sqrt(2 * np.pi))

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=eixo_x,
            y=densidade,
            mode="lines",
            fill="tozeroy",
            line=dict(color=COR_PRINCIPAL, width=3),
            name="Densidade"
        )
    )

    fig.update_layout(
        title="Densidade das Notas dos Produtos",
        xaxis_title="Nota do Produto",
        yaxis_title="Densidade",
        template="plotly_white"
    )

    return fig


def criar_regressao():
    dados = df[["Preço", "Nota", "Título", "Marca"]].dropna()

    coeficiente = np.polyfit(dados["Preço"], dados["Nota"], 1)
    linha = np.poly1d(coeficiente)

    x_linha = np.linspace(dados["Preço"].min(), dados["Preço"].max(), 100)
    y_linha = linha(x_linha)

    fig = px.scatter(
        dados,
        x="Preço",
        y="Nota",
        title="Regressão entre Preço e Nota dos Produtos",
        labels={"Preço": "Preço do Produto (R$)", "Nota": "Nota do Produto"},
        hover_data=["Título", "Marca"],
        color_discrete_sequence=[COR_PRINCIPAL]
    )

    fig.add_trace(
        go.Scatter(
            x=x_linha,
            y=y_linha,
            mode="lines",
            name="Linha de tendência",
            line=dict(color=COR_DESTAQUE, width=3)
        )
    )

    fig.update_traces(marker=dict(size=9, opacity=0.65), selector=dict(mode="markers"))
    fig.update_layout(template="plotly_white")

    return fig

# ======================================================
# 4. ESTATÍSTICAS PARA CARDS E INSIGHTS
# ======================================================

total_produtos = len(df)
nota_media = df["Nota"].mean()
preco_medio = df["Preço"].mean()
desconto_medio = df["Desconto"].mean()

marca_destaque = df["Marca"].value_counts().idxmax()
qtd_marca_destaque = df["Marca"].value_counts().max()

correlacao_preco_nota = df[["Preço", "Nota"]].corr().iloc[0, 1]
correlacao_avaliacoes_vendas = df[["N_Avaliações", "Qtd_Vendidos_Cod"]].corr().iloc[0, 1]

# ======================================================
# 5. CRIAÇÃO DA APLICAÇÃO DASH
# ======================================================

app = Dash(__name__)
app.title = "Dashboard de E-commerce"

# ======================================================
# 6. LAYOUT DA APLICAÇÃO
# ======================================================

app.layout = html.Div(
    style={
        "backgroundColor": COR_FUNDO,
        "fontFamily": "Arial, sans-serif",
        "padding": "30px"
    },
    children=[
        html.Div(
            style={
                "backgroundColor": COR_CARD,
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "marginBottom": "25px"
            },
            children=[
                html.H1(
                    "Dashboard de Análise de E-commerce",
                    style={"color": COR_TEXTO, "textAlign": "center"}
                ),
                html.P(
                    "Aplicação desenvolvida com Dash, Plotly e Pandas para visualizar os principais gráficos da análise exploratória dos produtos.",
                    style={
                        "color": "#4B5563",
                        "textAlign": "center",
                        "fontSize": "18px"
                    }
                )
            ]
        ),

        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gap": "20px",
                "marginBottom": "25px"
            },
            children=[
                html.Div(
                    [html.H3("Total de Produtos"), html.H2(f"{total_produtos}")],
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "20px",
                        "borderRadius": "12px",
                        "textAlign": "center"
                    }
                ),
                html.Div(
                    [html.H3("Nota Média"), html.H2(f"{nota_media:.2f}")],
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "20px",
                        "borderRadius": "12px",
                        "textAlign": "center"
                    }
                ),
                html.Div(
                    [html.H3("Preço Médio"), html.H2(f"R$ {preco_medio:.2f}")],
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "20px",
                        "borderRadius": "12px",
                        "textAlign": "center"
                    }
                ),
                html.Div(
                    [html.H3("Desconto Médio"), html.H2(f"{desconto_medio:.2f}%")],
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "20px",
                        "borderRadius": "12px",
                        "textAlign": "center"
                    }
                ),
            ]
        ),



        html.Div(
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "25px"
            },
            children=[
                html.Div(
                    dcc.Graph(figure=criar_histograma()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
                html.Div(
                    dcc.Graph(figure=criar_dispersao()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
                html.Div(
                    dcc.Graph(figure=criar_barras()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
                html.Div(
                    dcc.Graph(figure=criar_pizza()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
                html.Div(
                    dcc.Graph(figure=criar_mapa_calor()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
                html.Div(
                    dcc.Graph(figure=criar_densidade()),
                    style={
                        "backgroundColor": COR_CARD,
                        "padding": "15px",
                        "borderRadius": "12px"
                    }
                ),
            ]
        ),

        html.Div(
            style={
                "backgroundColor": COR_CARD,
                "padding": "15px",
                "borderRadius": "12px",
                "marginTop": "25px"
            },
            children=[
                dcc.Graph(figure=criar_regressao())
            ]
        ),

        html.Div(
            style={
                "backgroundColor": COR_CARD,
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "marginTop": "25px",
                "marginBottom": "25px"
            },
            children=[
                html.H2(
                    "📌 Principais Insights da Análise",
                    style={
                        "color": COR_TEXTO,
                        "textAlign": "center",
                        "marginBottom": "25px"
                    }
                ),

                html.Ul(
                    [
                        html.Li(
                            f"Foram analisados {total_produtos} produtos no conjunto de dados."
                        ),
                        html.Li(
                            f"A nota média dos produtos é {nota_media:.2f}, indicando avaliações geralmente positivas."
                        ),
                        html.Li(
                            f"O preço médio dos produtos é R$ {preco_medio:.2f}, com desconto médio de {desconto_medio:.2f}%."
                        ),
                        html.Li(
                            "As notas estão concentradas principalmente entre 4,2 e 4,9 estrelas."
                        ),
                        html.Li(
                            f"A marca {marca_destaque} possui a maior quantidade de produtos cadastrados, com {qtd_marca_destaque} itens."
                        ),
                        html.Li(
                            f"A correlação entre preço e nota é baixa ({correlacao_preco_nota:.2f}), sugerindo que produtos mais caros não necessariamente recebem melhores avaliações."
                        ),
                        html.Li(
                            f"A correlação entre número de avaliações e quantidade vendida é forte ({correlacao_avaliacoes_vendas:.2f}), indicando que produtos mais vendidos tendem a acumular mais avaliações."
                        ),
                    ],
                    style={
                        "fontSize": "18px",
                        "lineHeight": "2.1",
                        "paddingLeft": "30px",
                        "color": "#374151"
                    }
                )
            ]
        ),

        html.Div(
            style={
                "textAlign": "center",
                "marginTop": "30px",
                "color": "#6B7280"
            },
            children=[
                html.P("Projeto 3 - Visualização interativa com Dash e Plotly")
            ]
        )
    ]
)

# ======================================================
# 7. EXECUÇÃO DA APLICAÇÃO
# ======================================================

if __name__ == "__main__":
    app.run(debug=True)
