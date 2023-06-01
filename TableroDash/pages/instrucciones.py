# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from app import app
from apps import navigation
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dotenv import dotenv_values
import pandas as pd
import plotly.express as px
import psycopg2

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# VARIABLES CLASSIFICATION
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

diccionario_cat = {
    'Sexo': 'sex',
    'Tipo de dolor en el Pecho': 'cp',
    'Azucar en sangre en ayunas': 'fbs',
    'Resultados electrocardiograficos en reposo': 'restecg',
    'Angina inducida por ejercicio': 'exang',
    'Pendiente del segmento ST': 'slope',
    'Numero de vasos coloreados': 'ca',
    'Talasemia': 'thal',
    'Presencia de enfermedad cardiaca': 'heartdis'
}

diccionario_num = {
    'Edad': 'age',
    'Presión arterial en reposo': 'trestbps',
    'Colesterol serico': 'chol',
    'Frecuencia cardiaca maxima': 'thalach',
    'Depresión del segmento ST': 'oldpeak'
}

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Layout
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

instrucciones_layout = html.Div(children=[

    # ------------------------------------------------
    # Barra de Navegación
    # ------------------------------------------------

    navigation.navbar,
    html.Br(),

    # ------------------------------------------------
    # Titulo de la pagina
    # ------------------------------------------------

    html.H1(children='''¿Cómo se comportan las variables?''',
            style={'textAlign': 'center'}),
    html.Br(),

    # ------------------------------------------------
    # Categoricas vs Categoricas
    # ------------------------------------------------

    html.H4(children='''Graficas variables Categoricas vs Categoricas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                # Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x1',
                            options=[{'label': i, 'value': diccionario_cat[i]}
                                     for i in diccionario_cat],
                            value='sex'
                        )
                    ], style={'width': '30rem', 'display': 'inline-block'}),
                ),
                # Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y1',
                            options=[{'label': i, 'value': diccionario_cat[i]}
                                     for i in diccionario_cat],
                            value='cp'
                        )
                    ], style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
               'justify-content': 'center'}
    ),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catcat'),
        ]),
    html.Br(),

    # ------------------------------------------------
    # Categoricas vs Numericas
    # ------------------------------------------------

    html.H4(children='''Graficas variables Categoricas vs Numericas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                # Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x2',
                            options=[{'label': i, 'value': diccionario_cat[i]}
                                     for i in diccionario_cat],
                            value='sex'
                        )
                    ], style={'width': '30rem', 'display': 'inline-block'}),
                ),
                # Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y2',
                            options=[{'label': i, 'value': diccionario_num[i]}
                                     for i in diccionario_num],
                            value='age'
                        )
                    ], style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
               'justify-content': 'center'}
    ),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catnum'),
        ]),
    html.Br(),

    # ------------------------------------------------
    # Numericas vs Numericas
    # ------------------------------------------------

    html.H4(children='''Graficas variables Numericas vs Numericas''',
            style={'textAlign': 'center'}),
    html.Div(
        dbc.Row(
            [
                # Eje Y
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje X:'),
                        dcc.Dropdown(
                            id='graph-x3',
                            options=[{'label': i, 'value': diccionario_num[i]}
                                     for i in diccionario_num],
                            value='age'
                        )
                    ], style={'width': '30rem', 'display': 'inline-block'}),
                ),
                # Eje X
                dbc.Col(
                    html.Div([
                        html.Label('Seleccione un valor para el eje Y:'),
                        dcc.Dropdown(
                            id='graph-y3',
                            options=[{'label': i, 'value': diccionario_num[i]}
                                     for i in diccionario_num],
                            value='oldpeak'
                        )
                    ], style={'width': '30rem', 'float': 'right', 'display': 'inline-block'})
                ),
            ],
            className="mt-4",
        ),
        style={'display': 'flex',
               'justify-content': 'center'}
    ),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-numnum'),
        ]),
    html.Br(),
])

# -------------------------------------------------------------------------------------------------------------------
# CALLBACKS
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------
# Categoricas vs Categoricas
# ------------------------------------------------


@app.callback(
    Output('graphic-catcat', 'figure'),
    Input('graph-x1', 'value'),
    Input('graph-y1', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_cat = px.histogram(df, x=xaxis_column_name, y=yaxis_column_name,
                           color=yaxis_column_name, barmode='group', histfunc='count')

    return fig_cat

# ------------------------------------------------
# Categoricas vs Numericas
# ------------------------------------------------


@app.callback(
    Output('graphic-catnum', 'figure'),
    Input('graph-x2', 'value'),
    Input('graph-y2', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_bar = px.violin(df, x=xaxis_column_name, y=yaxis_column_name,
                        color=xaxis_column_name
                        )
    return fig_bar

# ------------------------------------------------
# Numericas vs Numericas
# ------------------------------------------------


@app.callback(
    Output('graphic-numnum', 'figure'),
    Input('graph-x3', 'value'),
    Input('graph-y3', 'value')
)
def update_graph(xaxis_column_name, yaxis_column_name):

    fig_disp = px.scatter(df, x=xaxis_column_name, y=yaxis_column_name)

    return fig_disp