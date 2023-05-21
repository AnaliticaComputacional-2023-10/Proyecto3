import dash_bootstrap_components as dbc
from dash import html
import dash

navbar = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row([
                        dbc.Col([
                            html.Img(src=dash.get_asset_url('analisis-de-datos.png'), height="40px"),
                            dbc.NavbarBrand("Analítica de Resultados Saber 11", className="ms-2")
                        ],
                        width={"size":"auto"})
                    ],
                    align="center",
                    className="g-0"),

                    dbc.Row([
                        dbc.Col([
                            dbc.Nav([
                                dbc.NavItem(dbc.NavLink("Inicio", href="/")),
                                dbc.NavItem(dbc.NavLink("Instrucciones", href="/instrucciones")),
                                dbc.NavItem(dbc.NavLink("Programa", href="/programa")),
                            ],
                            navbar=True
                            )
                        ],
                        width={"size":"auto"})
                    ],
                    align="center"),
                ],
            fluid=True
            ),
    color="primary",
    dark=True
)