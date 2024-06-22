from dash import html, dcc
import dash_bootstrap_components as dbc

layout1 = html.Div(children=[
    html.Div([
        "Select Cube",
        dcc.Dropdown(['Ideal Cube', 'Scrambled Cube'], 'Ideal Cube', id='cube_dropdown'),
        "Track moves",
        dcc.Dropdown(['Yes', 'No'], 'No', id='keep_track')
    ],
        style={
                "width": "10%",
                "marginLeft": "5em",
            },),
    html.Br(),
    html.Button("Reset", id="reset", n_clicks=0, style={'background-color': 'black', 'color': 'white'}),
    html.Br(),
    html.Div([
        dbc.Button("U_CW", id="Uw", n_clicks=0,
                   style={'background-color': 'white', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '150px'}),
        dbc.Button("U_CCW", id="Uw_inv", n_clicks=0,
                   style={'background-color': 'white', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'}),
        dbc.Button("F_CW", id="Fr", n_clicks=0,
                   style={'background-color': 'red', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '150px'}),
        dbc.Button("F_CCW", id="Fr_inv", n_clicks=0,
                   style={'background-color': 'red', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'}),
        dbc.Button("R_CW", id="Rb", n_clicks=0,
                   style={'background-color': 'blue', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '150px'}),
        dbc.Button("R_CCW", id="Rb_inv", n_clicks=0,
                   style={'background-color': 'blue', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'})
    ]),
    html.Div([
        dbc.Button("D_CW", id="Dy", n_clicks=0,
                   style={'background-color': 'yellow', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '170px'}),
        dbc.Button("D_CCW", id="Dy_inv", n_clicks=0,
                   style={'background-color': 'yellow', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'}),
        dbc.Button("B_CW", id="Bo", n_clicks=0,
                   style={'background-color': 'orange', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '150px'}),
        dbc.Button("B_CCW", id="Bo_inv", n_clicks=0,
                   style={'background-color': 'orange', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'}),
        dbc.Button("L_CW", id="Lg", n_clicks=0,
                   style={'background-color': 'green', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '150px'}),
        dbc.Button("L_CCW", id="Lg_inv", n_clicks=0,
                   style={'background-color': 'green', 'color': 'black', 'height': '50px', 'width': '100px',
                          'margin-top': '1px', 'margin-left': '50px'})
    ]),

    # html.Div(["\n\n\n\n"], style={"width": "100%", "marginLeft": "5em"}),
    html.Br(),
    html.Div(id='container'),
    html.Br(),
    html.Div([
        html.Button("Download CSV", id="btn_csv"),
        # dcc.Download(id="download-dataframe-csv"),
    ])

])
