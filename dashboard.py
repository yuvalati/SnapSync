import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Navbar(
        dbc.Container(fluid=True, children=[
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="Snapsync_logo.jpg", height="30px")),
                        dbc.Col(dbc.NavbarBrand("SnapSync", href="/"), class_name="ms-2"),
                    ],
                    align="center",
                    class_name="g-0",
                ),
                href="/",
                style={"textDecoration": "none"}
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("Profile", href="/profile")),
                    dbc.NavItem(dbc.NavLink("Discover", href="/discover")),
                    dbc.NavItem(dbc.NavLink("About", href="/about")),
                ],
                className="ms-auto", navbar=True
            ),
        ]),
        color="primary",
        dark=True,
        className="mb-5",
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col(html.Div("User Profile or Sync Information Here"), md=8),
            dbc.Col(html.Div("Map or Notifications Here"), md=4)
        ])
    ], fluid=True)
])

if __name__ == "__main__":
    app.run_server(debug=True)
