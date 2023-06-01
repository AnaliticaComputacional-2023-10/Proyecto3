# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from app import app
from apps import navigation
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.readwrite import BIFReader
import plotly.express as px


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LAYOUT
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

programa_layout = html.Div(children=[

    # ------------------------------------------------
    # Barra de Navegacion
    # ------------------------------------------------

    navigation.navbar,
    html.Br(),

    # ------------------------------------------------
    # Titulo de la pagina
    # ------------------------------------------------

    html.H1(children="Programa de Predicción Resuldatos Icfes",
            style={'textAlign': 'center'}),
    html.Br(),

    # ------------------------------------------------
    # Inicio Inputs Outpus
    # ------------------------------------------------

    dbc.Row([

        # ------------------------------------------------
        # Columna Inputs
        # ------------------------------------------------

        dbc.Col([html.Div("Información del Estudiante",
                          style={'font-weight': 'bold', 'font-size': 20}),

            # ------------------------------------------------
                 # Información del colegio
                 # ------------------------------------------------

                 dbc.Row([html.Div("Información del Colegio",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),

                 dbc.Row([

                     # ------------------------------------------------
                     # Colegio Rural
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El colegio esta ubicado en una zona: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Rural', 'value': '1'},
                                 {'label': 'Urbano', 'value': '0'}
                             ],
                             value='',
                             id='colegio_rural'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Colegio Bilingue
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El colegio al que asistio es bilingue: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '1'},
                                 {'label': 'No', 'value': '0'}
                             ],
                             value='',
                             id='colegio_bilingue'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'}),

                 dbc.Row([

                     # ------------------------------------------------
                     # Colegio Calendario
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El colegio es calendario: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'A', 'value': '1'},
                                 {'label': 'B', 'value': '2'},
                                 {'label': 'Otro', 'value': '3'}
                             ],
                             value='',
                             id='colegio_calendario'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Colegio Privado
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El colegio al que asistio es privado: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '1'},
                                 {'label': 'No', 'value': '0'}
                             ],
                             value='',
                             id='colegio_privado'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'}),

                 dbc.Row([

                     # ------------------------------------------------
                     # Colegio Genero
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El colegio es: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Mixto', 'value': '1'},
                                 {'label': 'Masculino', 'value': '2'},
                                 {'label': 'Femenino', 'value': '3'}
                             ],
                             value='',
                             id='colegio_genero'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Colegio Jornada
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('La jornada del colegio es: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Unica', 'value': '1'},
                                 {'label': 'Mañana', 'value': '2'},
                                 {'label': 'Tarde', 'value': '3'},
                                 {'label': 'Noche', 'value': '4'},
                                 {'label': 'Completa', 'value': '5'},
                                 {'label': 'Sabatina', 'value': '6'}
                             ],
                             value='',
                             id='colegio_jornada'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'}),

                 # ------------------------------------------------
                 # Información del estudiante
                 # ------------------------------------------------

                 dbc.Row([html.Div("Información del estudiante",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),
                 dbc.Row([

                     # ------------------------------------------------
                     # Estudiante Genero
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El estudiante es de genero: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Masculino', 'value': '1'},
                                 {'label': 'Femenino', 'value': '0'}
                             ],
                             value='',
                             id='estudiante_genero'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Estrato familia
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El estudiante es de estrato'),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Estrato 1', 'value': '1'},
                                 {'label': 'Estrato 2', 'value': '2'},
                                 {'label': 'Estrato 3', 'value': '3'},
                                 {'label': 'Estrato 4', 'value': '4'},
                                 {'label': 'Estrato 5', 'value': '5'},
                                 {'label': 'Estrato 6', 'value': '6'}
                             ],
                             value='',
                             id='familia_estrato'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'}),

                  dbc.Row([

                     # ------------------------------------------------
                     # Madre educación
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El nivel educativo de la madre es: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Ninguno', 'value': '1'},
                                 {'label': 'Primaria incompleta', 'value': '2'},
                                 {'label': 'Primaria completa', 'value': '3'},
                                 {'label': 'Secundaria (Bachillerato) incompleta', 'value': '4'},
                                 {'label': 'Secundaria (Bachillerato) completa', 'value': '5'},
                                 {'label': 'Técnica o tecnológica incompleta', 'value': '6'},
                                 {'label': 'Técnica o tecnológica completa', 'value': '7'},
                                 {'label': 'Educación profesional incompleta', 'value': '8'},
                                 {'label': 'Educación profesional completa', 'value': '9'},
                                 {'label': 'Postgrado', 'value': '10'}
                             ],
                             value='',
                             id='madre_educacion'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Padre educación
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('El nivel educativo del padre es: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Ninguno', 'value': '1'},
                                 {'label': 'Primaria incompleta', 'value': '2'},
                                 {'label': 'Primaria completa', 'value': '3'},
                                 {'label': 'Secundaria (Bachillerato) incompleta', 'value': '4'},
                                 {'label': 'Secundaria (Bachillerato) completa', 'value': '5'},
                                 {'label': 'Técnica o tecnológica incompleta', 'value': '6'},
                                 {'label': 'Técnica o tecnológica completa', 'value': '7'},
                                 {'label': 'Educación profesional incompleta', 'value': '8'},
                                 {'label': 'Educación profesional completa', 'value': '9'},
                                 {'label': 'Postgrado', 'value': '10'}
                             ],
                             value='',
                             id='padre_educacion'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'}),

                # ------------------------------------------------
                 # Acceso a tecnologia
                 # ------------------------------------------------

                 dbc.Row([html.Div("Acceso a tecnología",
                                   style={'font-weight': 'bold', 'font-size': 16, 'padding': '10px 25px'})]),

                  dbc.Row([

                     # ------------------------------------------------
                     # Computador
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Tiene computador en la casa: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '1'},
                                 {'label': 'No', 'value': '0'}
                             ],
                             value='',
                             id='computador'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Internet
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label('Tiene acceso a internet en la casa: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '1'},
                                 {'label': 'No', 'value': '0'}
                             ],
                             value='',
                             id='internet'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),
                 ], style={'padding': '10px 25px'})]),

        # ------------------------------------------------
        # Columna Outputs
        # ------------------------------------------------


        dbc.Col([

            # ------------------------------------------------
            # Texto Descripcion Paciente
            # ------------------------------------------------

            html.Div("Puntaje esperado de ICFES:",
                     style={'font-weight': 'bold', 'font-size': 20}),
            html.Br(),
            html.Div(' '*1000, id='data_patient'),
            html.Br(),
            html.Br(),

            # ------------------------------------------------
            # Boton Predecir Modelo
            # ------------------------------------------------

            dbc.Button(
                "Predecir Modelo",
                id="collapse-button",
                className="mb-3",
                color='primary',
                n_clicks=0
            ),
            html.Br(),

            # ------------------------------------------------
            # Boton Eliminar Inputs
            # ------------------------------------------------

            dbc.Button(
                'Eliminar inputs',
                id='button_eliminar',
                className="mb-3",
                color='primary',
                n_clicks=0
            ),

            # ------------------------------------------------
            # Grafica
            # ------------------------------------------------

            dcc.Graph(id='pie-chart'),
            html.Div(
                id='output2'
            )
        ],
            style={'padding': '10px 25px'}
        ),
    ]),
]
)






