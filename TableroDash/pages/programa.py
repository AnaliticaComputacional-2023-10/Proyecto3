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
                                 {'label': 'Urbana', 'value': '0'}
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

                 dbc.Row([

                     # ------------------------------------------------
                     # Colegio Municipio Distinto Residencia
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label(
                             'El colegio esta ubicado en el municipio que vive: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '0'},
                                 {'label': 'No', 'value': '1'}
                             ],
                             value='',
                             id='colegio_mcpio_distinto'
                         )
                     ]), width={"size": 3}, style={'margin-left': '50px'}),

                     # ------------------------------------------------
                     # Presentacion Municipio Distinto Residencia
                     # ------------------------------------------------

                     dbc.Col(html.Div([
                         html.Label(
                             'El examen fue presentado en el municipio en el que vive: '),
                         dcc.Dropdown(
                             options=[
                                 {'label': 'Si', 'value': '0'},
                                 {'label': 'No', 'value': '1'}
                             ],
                             value='',
                             id='presentacion_mcpio_distinto'
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
                                 {'label': 'Secundaria incompleta',
                                  'value': '4'},
                                 {'label': 'Secundaria completa',
                                  'value': '5'},
                                 {'label': 'Técnica incompleta',
                                     'value': '6'},
                                 {'label': 'Técnica completa',
                                     'value': '7'},
                                 {'label': 'Profesional incompleta',
                                     'value': '8'},
                                 {'label': 'Profesional completa',
                                     'value': '9'},
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
                                 {'label': 'Secundaria incompleta',
                                  'value': '4'},
                                 {'label': 'Secundaria completa',
                                  'value': '5'},
                                 {'label': 'Técnica incompleta',
                                     'value': '6'},
                                 {'label': 'Técnica completa',
                                     'value': '7'},
                                 {'label': 'Profesional incompleta',
                                     'value': '8'},
                                 {'label': 'Profesional completa',
                                     'value': '9'},
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
                 ], style={'padding': '10px 25px'})],

                width={"size": 6}, style={'marginLeft': '50px'}),

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
            html.Div(' '*1000, id='data_student'),
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

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LOAD THE MODEL
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

reader = BIFReader('./Models/Modelo.bif')
model = reader.get_model()
model.check_model()

infer = VariableElimination(model)

nodos = list(model.nodes)


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# FUNCTIONS THAT HELP
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------
# Funcion para Inferir
# ------------------------------------------------

def inferenceEvidence(evidence, infer):
    prob = infer.query(variables=['puntaje'], evidence=evidence)

    return prob.values.tolist()


# ------------------------------------------------
# Funcion para clasificar
# ------------------------------------------------

def getClassification(probs):
    maxi = 0
    clase = 0
    for i in range(0, 10):
        if probs[i] > maxi:
            maxi = probs[i]
            clase = i

    return clase


# ------------------------------------------------
# Funcion para generar Tablas
# ------------------------------------------------

def generateTable(lineas):
    rows = [html.Tr(linea) for linea in lineas]

    return html.Table(rows)

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# CONSTANTES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------
# Dictionary of variables meaning
# ------------------------------------------------


atributos = {
    'colegio_rural': 'Zona Colegio',
    'colegio_bilingue': 'Colegio Bilingue',
    'colegio_calendario': 'Tipo de calendario colegio',
    'colegio_privado': 'Colegio privado',
    'colegio_genero': 'Colegio genero',
    'colegio_jornada': 'Jornada del colegio',
    'estudiante_genero': 'Genero del estudiante',
    'familia_estrato': 'Estrato de la familia',
    'madre_educacion': 'Nivel educativo de la madre',
    'padre_educacion': 'Nivel educativo del padre',
    'computador': 'Cuenta con computador la familia',
    'internet': 'Cuenta con internet la familia',
    'colegio_mcpio_distinto': 'El colegio esta ubicado en el municipio que vive',
    'presentacion_mcpio_distinto': 'El estudiante presento el examen en el municipio que vive'
}

# ------------------------------------------------
# Dictionary of variables values interpretation
# ------------------------------------------------

significado = {
    'colegio_rural': {
        0: 'Colegio ubicado en zona urbana',
        1: 'Colegio ubicado en zona rural',
    },
    'colegio_bilingue': {
        0: 'El colegio NO es bilingue',
        1: 'El colegio es bilingue',
    },
    'colegio_calendario': {
        1: 'Colegio calendario A',
        2: 'Colegio calendario B',
        3: 'Colegio presenta otro tipo de calendario',
    },
    'colegio_privado': {
        0: 'El colegio NO es privado',
        1: 'El colegio es privado',
    },
    'colegio_genero': {
        1: 'El colegio es Mixto',
        2: 'El colegio es Masculino',
        3: 'El colegio es Femenino'
    },
    'colegio_jornada': {
        1: 'La jornada del colegio es Unica',
        2: 'La jornada del colegio es Mañana',
        3: 'La jornada del colegio es Tarde',
        4: 'La jornada del colegio es Noche',
        5: 'La jornada del colegio es Completa',
        6: 'La jornada del colegio es Sabatina',
    },
    'estudiante_genero': {
        0: 'El estudiante es de genero Femenino',
        1: 'El estudiante es de genero Masculino',
    },
    'familia_estrato': {
        1: 'La familia es de estrato 1',
        2: 'La familia es de estrato 2',
        3: 'La familia es de estrato 3',
        4: 'La familia es de estrato 4',
        5: 'La familia es de estrato 5',
        6: 'La familia es de estrato 6',
    },
    'madre_educacion': {
        1: 'La madre no tiene nivel educativo',
        2: 'La madre no completo primaria',
        3: 'La madre completo primaria',
        4: 'La madre no completo secundaria (Bachillerato)',
        5: 'La madre completo secundaria (Bachillerato)',
        6: 'La madre no completo técnica o tecnológica',
        7: 'La madre completo técnica o tecnológica',
        8: 'La madre no completo educación profesional',
        9: 'La madre completo educación profesional',
        10: 'La madre completo postgrado',
    },
    'padre_educacion': {
        1: 'La padre no tiene nivel educativo',
        2: 'La padre no completo primaria',
        3: 'La padre completo primaria',
        4: 'La padre no completo secundaria (Bachillerato)',
        5: 'La padre completo secundaria (Bachillerato)',
        6: 'La padre no completo técnica o tecnológica',
        7: 'La padre completo técnica o tecnológica',
        8: 'La padre no completo educación profesional',
        9: 'La padre completo educación profesional',
        10: 'La padre completo postgrado',
    },
    'computador': {
        0: 'La familia NO tiene computador',
        1: 'La familia tiene computador',
    },
    'internet': {
        0: 'La familia NO tiene acceso a internet',
        1: 'La familia tiene acceso a internet',
    },
    'colegio_mcpio_distinto': {
        0: 'El colegio esta ubicado en el mismo municipio en el que reside',
        1: 'El colegio NO esta ubicado en el mismo municipio en el que reside',
    },
    'presentacion_mcpio_distinto': {
        0: 'El estudiante presento el examen en el mismo municipio en el que reside',
        1: 'El estudiante NO presento el examen en el mismo municipio en el que reside',
    },
}

# ------------------------------------------------
# List of ranges
# ------------------------------------------------

rangos = [
    '0-50',
    '50-100',
    '100-150',
    '150-200',
    '200-250',
    '250-300',
    '300-350',
    '350-400',
    '400-450',
    '450-500',
]


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# INFERENCE
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

@app.callback(
    Output('data_student', 'children'),
    Output('pie-chart', 'figure'),
    State('colegio_rural', 'value'),
    State('colegio_bilingue', 'value'),
    State('colegio_calendario', 'value'),
    State('colegio_privado', 'value'),
    State('colegio_genero', 'value'),
    State('colegio_jornada', 'value'),
    State('colegio_mcpio_distinto', 'value'),
    State('presentacion_mcpio_distinto', 'value'),
    State('estudiante_genero', 'value'),
    State('familia_estrato', 'value'),
    State('madre_educacion', 'value'),
    State('padre_educacion', 'value'),
    State('computador', 'value'),
    State('internet', 'value'),
    Input('collapse-button', 'n_clicks'))
def generate_matrix(
        colegio_rural,
        colegio_bilingue,
        colegio_calendario,
        colegio_privado,
        colegio_genero,
        colegio_jornada,
        colegio_mcpio_distinto,
        presentacion_mcpio_distinto,
        estudiante_genero,
        familia_estrato,
        madre_educacion,
        padre_educacion,
        computador,
        internet,
        n_clicks):

    # ------------------------------------------------
    # Mensaje Introduccion Usuario
    # ------------------------------------------------

    if n_clicks == 0:
        lineas = [
            'Llene sus datos en las opciones.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Dictionary of variables values
    # ------------------------------------------------

    valores = {
        'colegio_rural': colegio_rural,
        'colegio_bilingue': colegio_bilingue,
        'colegio_calendario': colegio_calendario,
        'colegio_privado': colegio_privado,
        'colegio_genero': colegio_genero,
        'colegio_jornada': colegio_jornada,
        'colegio_mcpio_distinto': colegio_mcpio_distinto,
        'presentacion_mcpio_distinto': presentacion_mcpio_distinto,
        'estudiante_genero': estudiante_genero,
        'familia_estrato': familia_estrato,
        'madre_educacion': madre_educacion,
        'padre_educacion': padre_educacion,
        'computador': computador,
        'internet': internet,
    }

    # ------------------------------------------------
    # Dictionary of variable values filtered by not empty
    # ------------------------------------------------

    valores_filtrados = {key: value
                         for (key, value) in valores.items()
                         if value != '' and value is not None}

    # ------------------------------------------------
    # Dictionary of variable values discretized
    # ------------------------------------------------

    discrete_valores = valores_filtrados.copy()

    # ------------------------------------------------
    # Filter the evidence with the nodes of the model
    # ------------------------------------------------

    discrete_valores_nodes = {key: value
                              for (key, value) in discrete_valores.items()
                              if key in nodos}

    # ------------------------------------------------
    # Filter the evidence with the nodes of the model
    # ------------------------------------------------

    evidence = {key: str(value)
                for (key, value) in discrete_valores_nodes.items()}

    # ------------------------------------------------
    # Sin evidencia, no se hace inferencia
    # ------------------------------------------------

    if evidence == {}:
        lineas = [
            'Seleccione los datos que conoce.',
            'Una vez ha llenado los datos conocidos presione el botón -Predecir Modelo-.',
            '-',
            'Nota: No es necesario conocer todos los datos, con al menos uno bastará.'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Inferencia con la evidencia
    # ------------------------------------------------

    try:
        probs = inferenceEvidence(evidence, infer)
        rango = rangos[getClassification(probs)]
    except:
        probs = None

    # ------------------------------------------------
    # Error en la inferencia
    # ------------------------------------------------

    if probs is None:
        lineas = [
            'Dados los siguientes parámetros: '
        ] + [
            f'{atributos[key]}: {significado[key][int(value)]}'
            for (key, value) in evidence.items()
        ] + [
            '-',
            f'El puntaje esperado para el estudiante no es posible calcularla ya que no hay suficientes datos'
        ]
        fig = px.pie()

        return generateTable(lineas), fig

    # ------------------------------------------------
    # Mensaje Resultado Usuario
    # ------------------------------------------------

    lineas = [
        'Dados los siguientes parámetros: '
    ] + [
        f'{significado[key][int(value)]}'
        for (key, value) in evidence.items()
    ] + [
        '-',
        f'El puntaje esperado para el estudiante está entre: {rango}'
    ]

    # ------------------------------------------------
    # Grafico
    # ------------------------------------------------

    df_graph = pd.DataFrame(
        {'rango': rangos,
         'probabilidad': probs
         }
    )

    fig = px.bar(
        data_frame=df_graph,
        y='rango',
        x='probabilidad',
        orientation='h',
        title='Probabilidad de que el puntaje esté en un rango',
        color_discrete_sequence=['#F97B72', '#80B1D3'],
    )

    fig.update_yaxes(
        title_text='Rango Puntaje',
    )

    fig.update_xaxes(
        title_text='Probabilidad',
    )

    fig.update_layout(
        legend_title='',
        # height=250,
        xaxis_range=[0, 1]
    )

    return generateTable(lineas), fig


# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# CLEAR
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------
# Clear Inputs
# ------------------------------------------------

@app.callback(Output('colegio_rural', 'value'),
              Output('colegio_bilingue', 'value'),
              Output('colegio_calendario', 'value'),
              Output('colegio_privado', 'value'),
              Output('colegio_genero', 'value'),
              Output('colegio_jornada', 'value'),
              Output('estudiante_genero', 'value'),
              Output('familia_estrato', 'value'),
              Output('madre_educacion', 'value'),
              Output('padre_educacion', 'value'),
              Output('computador', 'value'),
              Output('internet', 'value'),
              Output('colegio_mcpio_distinto', 'value'),
              Output('presentacion_mcpio_distinto', 'value'),
              [Input('button_eliminar', 'n_clicks')])
def clear_inputs(n_clicks):

    if n_clicks is not None:
        return '', '', '', '', '', '', '', '', '', '', '', '', '', ''


# ------------------------------------------------
# Clear Output
# ------------------------------------------------

@app.callback(Output('output2', 'children'),
              [Input('button_eliminar', 'n_clicks')])
def clear_output(n_clicks):
    if n_clicks == 0:
        return ''
