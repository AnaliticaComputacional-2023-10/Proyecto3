from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''  '''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas.'

inicio_layout = html.Div(children=[

    #Barra de Navegación
    navigation.navbar,
    html.Br(),

    #Titulo de la pagina
    html.H1(children = '''Bienvenido a la aplicación para la predicción de resultados en la prueba Saber 11''',
            style={'textAlign': 'center', 'margin-left': '20px'}),
    html.Br(),

    html.Br(),

    #Parrafo
    html.Div(children=[
        html.Img(src='/assets/examen.png', style={'height': '20%', 'width': '20%','margin-right':'10px'}),
        html.Div(children=[
            html.Pre(texto, style={'text-align': 'center','padding':'1px'})
        ], style={'margin-left': '10px'})
    ],
    style={'display': 'flex',
           'align-items': 'center',
           'justify-content': 'flex-start',
           'margin-left': '130px'}),
    html.Br(),
    html.Br(),
    html.Div(html.Pre(texto3, style={'text-align': 'center'}))
])