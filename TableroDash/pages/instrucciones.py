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
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import psycopg2

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------
# Mostrar el resultado como un pandas DataFrame
# ------------------------------------------------

# Ejecutar la query

def execute(query: str, cursor: (psycopg2.extensions.cursor)):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


# Hallar los atributos

def getColumnNames(cursor):
    columns = [i[0] for i in cursor.description]
    return columns


# Mostrar como DataFrame

def pdsql(query: str, connection: (psycopg2.extensions.connection)):
    try:
        cursor = connection.cursor()
        result = execute(query, cursor)
        columns = getColumnNames(cursor)
        df = pd.DataFrame(result, columns=columns)
        return df
    except Exception:
        connection.commit()
        return "Query Error"


# ------------------------------------------------
# Get the credentials of the database
# ------------------------------------------------

env_path = './env/graficas.env'

env_vars = dotenv_values(dotenv_path=env_path)

HOST = env_vars['HOST']
PORT = env_vars['PORT']
USER = env_vars['USER']
PASSWORD = env_vars['PASSWORD']
DBNAME = env_vars['DBNAME']


# ------------------------------------------------
# Connect to the database
# ------------------------------------------------

connection = psycopg2.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    dbname=DBNAME,
)


# ------------------------------------------------
# Get the data from the database
# ------------------------------------------------

# Grafica 1 - Departamentos

query = """
SELECT *
FROM promedio_departamento
;
"""
df_departamento = pdsql(query, connection)

# Grafica 2 - Zona

query = """
SELECT *
FROM promedio_zona
;
"""
df_zona = pdsql(query, connection)

# Grafica 3 - Estrato

query = """
SELECT *
FROM promedio_estrato
;
"""
df_estrato = pdsql(query, connection)


# ------------------------------------------------
# Close connection to the database
# ------------------------------------------------

connection.close

# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# Graficas
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------
# Mapa
# ------------------------------------------------

# df_departamento.loc[21, 'nombre'] = 'NARIÃ‘O'

file = open('./Data/Original/ColombiaGeo.json')
counties = json.load(file)
file.close()
locs = df_departamento['nombre']

for loc in counties['features']:
    loc['id'] = loc['properties']['NOMBRE_DPT']

fig_mapa = go.Figure(
    go.Choroplethmapbox(
        geojson=counties,
        locations=locs,
        z=df_departamento['punt_promedio'],
        colorscale='Reds',
        colorbar_title="Puntaje Promedio"
    )
)

fig_mapa.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=4.7,
    mapbox_center={"lat": 4.570868, "lon": -74.2973328},
    width=900,
    height=900
)

# ------------------------------------------------
# Zona
# ------------------------------------------------

fig_zona = px.bar(
    data_frame=df_zona,
    y='zona',
    x='punt_promedio',
    color='tipo',
    orientation='h',
    barmode='group'

)
fig_zona.update_layout(
    xaxis_range=[0, 500],
    legend_title_text='Tipo'
)
fig_zona.update_xaxes(
    title='Puntaje Promedio'
)
fig_zona.update_yaxes(
    title='Zona Ubicación'
)

# ------------------------------------------------
# Estrato
# ------------------------------------------------

fig_estrato = px.bar(
    data_frame=df_estrato,
    y='estrato',
    x='punt_promedio',
    # color='cole_naturaleza',
    orientation='h',
    # barmode='group'
)
fig_estrato.update_layout(
    xaxis_range=[0, 500]
)

fig_estrato.update_xaxes(
    title='Puntaje Promedio'
)
fig_estrato.update_yaxes(
    title='Estrato'
)

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
            dcc.Graph(
                id='graphic-catcat',
                figure=fig_mapa
            ),
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
            dcc.Graph(
                id='graphic-numnum',
                figure=fig_zona),
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
            dcc.Graph(
                id='graphic-catnum',
                figure=fig_estrato
            ),
        ]),
    html.Br(),
])
