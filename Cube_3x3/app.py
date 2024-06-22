import dash
# import dash_bootstrap_components as dbc

# https://towardsdatascience.com/beginners-guide-to-building-a-multi-page-dashboard-using-dash-5d06dbfc7599
# tutorial on dash for beginners
# bootstrap theme
# https://bootswatch.com/lux/
# external_stylesheets = [dbc.themes.LUX]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True