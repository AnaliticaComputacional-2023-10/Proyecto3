# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# LIBRARIES
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

from dash import html
from apps import navigation
import dash_bootstrap_components as dbc

texto = '''Los resultados del ICFES son de suma importancia para el sistema educativo
 y la sociedad en general. Estas pruebas brindan una evaluación objetiva de los conocimientos
 y habilidades de los estudiantes, permitiendo identificar fortalezas y debilidades en el
 proceso de aprendizaje. Los resultados del ICFES son una herramienta fundamental para tomar
 decisiones informadas en cuanto a la calidad de la educación, la implementación de políticas
 educativas y la asignación de recursos. Además, estos resultados sirven como referencia para
 las instituciones educativas, los padres y los propios estudiantes, ya que les proporcionan
 una medida clara de su desempeño académico en comparación con otros estudiantes a nivel nacional.
 Asimismo, los resultados del ICFES son utilizados por las universidades como criterio de admisión,
 lo que resalta aún más su importancia en el ámbito educativo.

Este programa se ha desarrollado mediante la exploración de datos y el modelado con
redes bayesianas, con el fin de descubrir la relación entre 19 atributos relevantes en la base
de datos de los resultados del ICFES.'''

texto3 = 'Aplicación creada por Santiago González y Juliana Cárdenas.'

card_graficas = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardLink(
                [
                    html.Img(src='/assets/presentacion-grafica.png', height=65),
                    html.Span("Información Descriptiva",
                              className="ms-2", style={"color": "white"})
                ],
                className="text-decoration-none h2",
                href="/instrucciones"
            )
        ]
    ),
    className="shadow my-2",
    style={"maxWidth": 500, "background-color": "#FEC868"},
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
    style={"maxWidth": 500, "background-color": "#ABC270"},
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

    html.H1(children='''Bienvenido al Programa de Predicción de Enfermedades Cardíacas''',
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
    html.Div(html.Pre(texto3, style={'text-align': 'center'}))
])

