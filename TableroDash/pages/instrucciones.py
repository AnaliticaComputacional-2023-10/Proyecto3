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
import plotly.graph_objects as go
import psycopg2

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

    html.H1(children='''Información descriptiva''',
            style={'textAlign': 'center'}),
    html.Br(),

    # ------------------------------------------------
    # Mapa Colombia
    # ------------------------------------------------

    html.H4(children='''Puntaje de ICFES según el departamento en el que te encuentres''',
            style={'textAlign': 'center'}),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catcat'),
        ]),
    html.Br(),

    # ------------------------------------------------
    # Estrato
    # ------------------------------------------------

    html.H4(children='''Puntaje de ICFES según el estrato en el que estes''',
            style={'textAlign': 'center'}),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-catnum'),
        ]),
    html.Br(),

    # ------------------------------------------------
    # Zona
    # ------------------------------------------------

    html.H4(children='''Puntaje de ICFES según la zona en la que se encuentra ubicado tu colegio''',
            style={'textAlign': 'center'}),

    # Grafica
    html.Div(
        style={'textAlign': 'center',
               'margin': '50px auto', 'maxWidth': '1200px'},
        children=[
            dcc.Graph(id='graphic-numnum'),
        ]),
    html.Br(),
])
