# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''
 Los resultados de la Prueba Saber 11 son de suma importancia para tu futuro, por esto 
 es importante que entiendas antes de presentar el examen como te podría ir en este.
 
 
 Primero, te mostramos algunas estadísticas interesantes sobre el puntaje promedio en estas 
 pruebas.
 Podrás comparar por:
 - Departamento
 - Colegio en la Ciudad o Rural
 - Estrato
 
 Estos gráficos pueden darte una idea de lo que puedes esperar de tu puntaje, dado 
 el departamento en que vives, el colegio en que estás y el estrato de tu hogar.
 
 Finalmente, deberás llenar cierta información de tu colegio, de tu familia y de tu hogar. 
 Con esto podrás obtener un rango de puntos que puedes obtener en el examen.
'''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas.'

card_graficas = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src='/assets/presentacion-grafica.png', height=65),
                    html.Span("Gráficas",
                              className="ms-2", style={"color": "white"})
                ],
                className="text-decoration-none h2",
                href="/instrucciones"
            )
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 500, "background-color": "#9DB2BF"},
)


card_modelo = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src='/assets/analisis-de-datos.png', height=65),
                    html.Span("Modelo Predictivo",
                              className="ms-2", style={"color": "white"})
                ],
                className="text-decoration-none h2",
                href="/programa"
            )
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 500, "background-color": "#9DB2BF"},
)

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LAYOUT
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


inicio_layout = html.Div(children=[

    # ------------------------------------------------
    # Barra de Navegacion
    # ------------------------------------------------

    navigation.navbar,
    html.Br(),

    # ------------------------------------------------
    # Titulo
    # ------------------------------------------------

    html.H1(children='''Bienvenido Estudiante''',
            style={'textAlign': 'center'}),
    html.Br(),

    html.Br(),

    # ------------------------------------------------
    # Parrafo Descripcion
    # ------------------------------------------------

    html.Div(children=[
        html.Img(src='/assets/img1.png',
                 style={'height': '20%', 'width': '20%', 'margin-right': '10px'}),
        html.Div(children=[
            html.Pre(texto, style={'text-align': 'center', 'padding': '1px'})
        ], style={'margin-left': '10px'})
    ],
        style={'display': 'flex',
               'align-items': 'center',
               'justify-content': 'flex-start',
               'margin-left': '130px'}),
    html.Br(),
    html.Br(),

    # ------------------------------------------------
    # Cards
    # ------------------------------------------------

    html.Div(children=[

        # ------------------------------------------------
        # Graficas
        # ------------------------------------------------

        html.Div(children=[
            dbc.Container(card_graficas)],
        ),

        # ------------------------------------------------
        # Programa
        # ------------------------------------------------

        html.Div(children=[
            dbc.Container(card_modelo)],
        ),
    ],
        style={'margin-bottom': '10px',
               'display': 'flex',
               'justify-content': 'center'}),
    html.Br(),
    html.Div(html.Pre(texto3, style={
             'text-align': 'center', 'font-weight': 'bold'}))
])
