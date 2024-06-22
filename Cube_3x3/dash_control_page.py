import numpy as np
# from app import app
import dash
import csv
from dash import Input, Output, ctx
from app_layout import layout1
from basic_structure import RubiksCube3x3
from dash import html, dcc
# import pandas as pd

Rubie = RubiksCube3x3()
app = dash.Dash(__name__)
app.layout = layout1

@app.callback(
    Output('container', 'children'),
    # Output('download-dataframe-csv', 'data'),
    [Input('cube_dropdown', 'value'),
    Input('keep_track', 'value'),
    Input('reset', 'n_clicks'),
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
    Input('Lg_inv', 'n_clicks'),
    Input("btn_csv", "n_clicks"),])
def rubie_transitions(cube_dropdown, keep_track, reset, Uw, Uw_inv, Fr, Fr_inv, Rb, Rb_inv, Dy, Dy_inv, Bo, Bo_inv, Lg,
                      Lg_inv, btn_csv):
    # Rubie = RubiksCube3x3()
    # ctx = dash.callback_context
    button_id = ctx.triggered_id if not None else 'No clicks yet'
#     # print(button_id)
    if button_id == 'cube_dropdown':
        if cube_dropdown == 'Ideal Cube':
            Rubie.initial_state = 0
            Rubie.cube = Rubie.construct_ideal_cube()
        else:
            Rubie.initial_state = -1
            Rubie.scramble_ideal_cube()
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'keep_track':
        print(keep_track)
        if keep_track == 'Yes':
            Rubie.track_moves = True
        else:
            Rubie.track_moves = False
            Rubie.move_sequences = []
            Rubie.cubies_moves = {'UBL': [], 'UFL': [], 'UFR': [], 'URB': [],
                                 'DBL': [], 'DFL': [], 'DFR': [], 'DRB': [],
                                 'UL': [], 'UF': [], 'UR': [], 'UB': [],
                                 'BL': [], 'LF': [], 'FR': [], 'RB': [],
                                 'DL': [], 'DF': [], 'DR': [], 'DB': [],
                                 'U': [], 'D': [], 'F': [], 'B': [], 'L': [], 'R': []}
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'reset':
        # Rubie1 = RubiksCube3x3()
        if Rubie.initial_state == 0:
            Rubie.cube = Rubie.construct_ideal_cube()
        else:
            Rubie.scramble_ideal_cube()
        cubies_moves = {'UBL': [], 'UFL': [], 'UFR': [], 'URB': [],
                        'DBL': [], 'DFL': [], 'DFR': [], 'DRB': [],
                        'UL': [], 'UF': [], 'UR': [], 'UB': [],
                        'BL': [], 'LF': [], 'FR': [], 'RB': [],
                        'DL': [], 'DF': [], 'DR': [], 'DB': []}
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw':
        # print(button_id)
        Rubie.rotate_layer('u', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Uw')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Uw_inv':
        Rubie.rotate_layer('u', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Uw_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Fr':
        # print(button_id)
        Rubie.rotate_layer('f', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Fr')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Fr_inv':
        Rubie.rotate_layer('f', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Fr_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Rb':
        # print(button_id)
        Rubie.rotate_layer('r', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Rb')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Rb_inv':
        Rubie.rotate_layer('r', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Rb_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Dy':
        # print(button_id)
        Rubie.rotate_layer('d', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Dy')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Dy_inv':
        Rubie.rotate_layer('d', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Dy_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Bo':
        # print(button_id)
        Rubie.rotate_layer('b', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Bo')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Bo_inv':
        Rubie.rotate_layer('b', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Bo_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Lg':
        # print(button_id)
        Rubie.rotate_layer('l', -90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Lg')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'Lg_inv':
        Rubie.rotate_layer('l', 90)
        if Rubie.track_moves is True:
            Rubie.appending_move()
            Rubie.move_sequences.append('Lg_inv')
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out
    elif button_id == 'btn_csv':
        if Rubie.track_moves is True:
            with open('cubies_moves.csv', 'w') as f:
                f.write("%s,%s\n" % ('moves', Rubie.move_sequences))
                for key in Rubie.cubies_moves.keys():
                    f.write("%s,%s\n" % (key, Rubie.cubies_moves[key]))
            f.close()
        else:
            print('track moves option is off, hence no file is saved')
    else:
        fig = Rubie.display_cube()
        fig.layout['uirevision'] = True
        update_out = html.Div([
            html.Div([dcc.Graph(id='graph_3d', figure=fig)], style={'width': '49%', 'display': 'inline-block'})],
            style={'display': 'flex'})
        return update_out


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True, port='8088', use_reloader=True)