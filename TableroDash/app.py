import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
app.title = 'Resultados Saber 11'
app._favicon = ("modelo.ico")
server = app.server
