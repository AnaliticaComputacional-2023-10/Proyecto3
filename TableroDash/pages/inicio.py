from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = ''' gvliyvliyvliuyvfliu '''

card_graficas = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src='/assets/presentacion-grafica.png', height=65),
                    html.Span("Información Descriptiva",
                              className="ms-2")
                ],
                className="text-decoration-none h2",
                href="/instrucciones"
            ),
            html.Hr(),
            html.Div("Remote, Canada", className="small"),
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 450},
)

card_modelo = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src='/assets/analisis-de-datos.png', height=65),
                    html.Span("Modelo Predictivo",
                              className="ms-2")
                ],
                className="text-decoration-none h2",
                href="/programa"
            ),
            html.Hr(),
            html.Div("Remote, Canada", className="small"),
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 550},
)

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
    html.Div(
        [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Container(card_graficas),
                        dbc.Container(card_modelo),
                    ]
                ),
                dbc.Col(html.Div(html.Pre(texto, style={'text-align': 'center'})))
            ]
        ),
    ],
    style={'display': 'flex',
           'align-items': 'center',
           'justify-content': 'flex-start',
           'margin-left': '200px'}),



    html.Br(),
    html.Div(html.Pre('Aplicación creada por Santiago González y Juliana Cárdenas.', style={'text-align': 'center'}))
])