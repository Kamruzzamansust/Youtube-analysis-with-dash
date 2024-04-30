
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import dash
#import dash_canvas
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import graphs

dash.register_page(__name__, path = '/page-1', name =  'page1')

row_1 = dbc.Row(
    [
        dbc.Col(
            [
             html.H2 ('Geo-Map-Scatter Map Box',style = {'text-align':'center'})
            ]
        ),
        
    ],style ={'height':'50px',
              'backgroundColor':'gray'}
)

row_2 = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Graph(id = 'worldmap',figure = graphs.fig6)
            ]
        )
    ],style={'height':'900px',
    'backgroundColor':'white'}
)


layout=dbc.Container(
    [
        row_1,
        row_2
    ],fluid=True, style={'height':'1450px'
                          ,'border':'2px solid green',
                          'backgroundColor':'white'
                          
                          }
)