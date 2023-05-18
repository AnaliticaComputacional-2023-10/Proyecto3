import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = 'Resultados Saber 11'
server = app.server
