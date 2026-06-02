from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv(r"C:\Users\ander\Downloads\ecommerce_estatistica.csv")


#Histograma
fig_hist = px.histogram(
    df,
    x='Preço',
    nbins=20,
    title='Distribuição dos Preços'
)

#Scatter
fig_scatter = px.scatter(
    df,
    x='Preço',
    y='Nota',
    color='Gênero',
    size='N_Avaliações',
    title='Preço x Nota'
)

#Boxplot
fig_box = px.box(
    df,
    x='Gênero',
    y='Preço',
    color='Gênero',
    title='Preço por Gênero'
)

#Barras
preco_genero = (
    df.groupby('Gênero')['Preço']
    .mean()
    .reset_index()
)

fig_bar = px.bar(
    preco_genero,
    x='Gênero',
    y='Preço',
    color='Gênero',
    title='Preço Médio por Gênero'
)

#Pizza
fig_pie = px.pie(
    df,
    names='Gênero',
    title='Distribuição dos Produtos por Gênero'
)

#Heatmap
corr = df[
    ['Preço', 'Nota', 'Desconto', 'N_Avaliações']
].corr()

fig_heat = px.imshow(
    corr,
    text_auto=True,
    title='Mapa de Correlação'
)

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        'Dashboard Ecommerce Estatistica - Atividade 3',
        style={
            'textAlign': 'center',
            'marginBottom': '30px'
        }
    ),

    dcc.Graph(figure=fig_hist),

    dcc.Graph(figure=fig_scatter),

    dcc.Graph(figure=fig_box),

    dcc.Graph(figure=fig_bar),

    dcc.Graph(figure=fig_pie),

    dcc.Graph(figure=fig_heat)

])

if __name__ == '__main__':
    app.run(debug=True)