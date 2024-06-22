import json
import dash_bootstrap_components as dbc
import dash
import dash_html_components as html
from dash import Input, Output, ctx, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        "Select Cube",
        dcc.Dropdown(['Ideal Cube', 'Scrambled Cube'], 'Ideal Cube', id='cube_dropdown')]),
    html.Button("Reset", id="reset", n_clicks=0, style={'background-color': 'black', 'color': 'white'}),
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
                      'margin-top': '1px', 'margin-left': '50px'}),
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
                      'margin-top': '1px', 'margin-left': '50px'}),
    html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              [Input('cube_dropdown', 'value'),
               Input('Uw', 'n_clicks'),
               Input('Uw_inv', 'n_clicks'),
               Input('Fr', 'n_clicks'),
               Input('Fr_inv', 'n_clicks'),
               Input('Rb', 'n_clicks'),
               Input('Rb_inv', 'n_clicks'),
               Input('Dy', 'n_clicks'),
               Input('Dy_inv', 'n_clicks'),
               Input('Bo', 'n_clicks'),
               Input('Bo_inv', 'n_clicks'),
               Input('Lg', 'n_clicks'),
               Input('Lg_inv', 'n_clicks')])
def display(cube_dropdown, Uw, Uw_inv, Fr, Fr_inv, Rb, Rb_inv, Dy, Dy_inv, Bo, Bo_inv, Lg, Lg_inv):
    # ctx = dash.callback_context

    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(button_id)
    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([html.Th('Button 1'),
                     html.Th('Button 2'),
                     html.Th('Button 3'),
                     html.Th('Most Recent Click')]),
            html.Tr([html.Td(Uw or 0),
                     html.Td(Fr or 0),
                     html.Td(Rb or 0),
                     html.Td(Dy or 0),
                     html.Td(button_id)])
        ]),
        html.Pre(ctx_msg)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)