#dash.get_asset_url('cells.png')
import dash
from dash import html, dcc,Input,Output,State, callback
#import dash_bootstrap_components as dbc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import dash
#import dash_canvas
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd 
import dash_table
import re
import numpy as np
import plotly.colors as colors
import style  as st
import graphs
from plotly.subplots import make_subplots



app = dash.Dash(
    __name__,use_pages= True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

df = pd.read_csv("Global YouTube Statistics.csv",encoding='latin-1')
df['category'].fillna("Not Found", inplace=True)
df['Country'].fillna("Not Found", inplace=True)
df['Abbreviation'].fillna("Not Found", inplace = True)
df['channel_type'].fillna("Not Found", inplace = True)
df.drop('country_rank', axis=1, inplace=True)
df['channel_type_rank'].fillna('Not Found',inplace = True)
df['video_views_for_the_last_30_days'].fillna('Not Found',inplace = True)
df['subscribers_for_last_30_days'].fillna('Not Found',inplace = True)
df['Gross tertiary education enrollment (%)'].fillna('Not Found',inplace = True)
df['Population'].fillna('Not Found',inplace = True)
df['Urban_population'].fillna('Not Found',inplace = True)
df['Latitude'].fillna('Not Found',inplace = True)
df['Longitude'].fillna('Not Found',inplace = True)
df['Unemployment rate'].fillna('Not Found',inplace = True)
# # df['created_year'] =df['created_year'].astype(int)
# # print(df['created_year'])
# df['Year'] = df['created_year'].apply(lambda x: x.strftime('%Y'))
df['Year'] = pd.to_datetime(df['created_year'], format='%Y', errors='coerce')

df['Year'] = pd.to_numeric(df['Year'].dt.year, errors='coerce').astype(pd.Int64Dtype())
df['Year'] = df['Year'].astype(str)
df = df[df['Year'] != "1970"]

df.dropna(inplace=True)



image_urls = [
    
    #"png-transparent-youtube-logo-wistia-television-channel-youtube-television-text-trademark-removebg-preview.png",
    #"png-transparent-youtube-logo-wistia-television-channel-youtube-television-text-trademark-removebg-preview.png",
    #"movie-theater.avif",
    "download.png",
    "apple-music-note.jpg",
    "images.jpg",
   # "png-clipart-computer-icons-information-data-chart-trend-lines-angle-text-thumbnail.png",
    "science.jpg",
    "Lifecycle 01-1.webp"

   

    
]







row_1 = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Button(
                    
                    children = [

                    html.Img(src=dash.get_asset_url('588a6507d06f6719692a2d15.png'), width=35, height=30),

                    html.Span("Menu", style={'margin-left': '10px'})


                ] ,

                id="open-offcanvas-button", color="white"),


                dbc.Offcanvas(


                    children=[


                        html.H2("Index", className="display-4"),

                        html.Hr(),
                         html.Img(src=dash.get_asset_url('png-transparent-youtube-logo-wistia-television-channel-youtube-television-text-trademark.png'),
                                   style = {'backgroundColor':'#F8F0E5',
                                                                   'margin-right':'20px',
                                                                    'width':'100px',
                                                                     'height':'70px'}),
                        # html.P(

                        #     "A simple sidebar layout with navigation links",

                        #     className="lead",
                        # ),


                        dbc.Nav(
                            [
                                dbc.NavLink("Overview", href="/",style={'color': 'red'}),

                                dbc.NavLink("Page 1", href="/page-1",style={'color': 'red'}),

                                dbc.NavLink("Page 2", href="/page-2",style={'color': 'red'}),
                            ],

                            vertical=True,

                           # pills=True,

                        ),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Br(),
                        html.Hr(),

                        html.Img(
                            
                            
                                id="image-display", 
                                 src=image_urls[0],
                                width=350, height=200,
                                 style = {'backgroundColor':'#F8F0E5'}
                                 
                                 
                                 ),


                         dcc.Interval(
                             
                        id="interval-component",

                        interval=3 * 1000,  # 5 seconds in milliseconds

                         n_intervals=0





    ),
                        html.Hr(),
            #              dbc.Row(
            #     [
            #                             dcc.Dropdown(
            # id='Country-Dropdown',

            #  options=list(df['Country'].unique()) + ["ALL"], 
            #  value='ALL',  
            #  multi=False,
            #  style={'width': '300px',
            #            'margin-top':'10px'})


            #     ],style = {'margin-top':'50px'}
            #   ),








                    ],
                    id="offcanvas",

                    #title="Offcanvas sidebar",

                    is_open=False,

                    scrollable=True,

                    style={"backgroundColor": "#F8F0E5",
                          'border':'5px solid red'}
                ),

                              




            ],width = 2,

        ),

    ],
    
    style = {'backgroundColor':'#df1b1b',
               'height':'50px'}

)


row_2 = dbc.Row(
    [
         dbc.Col(
                          [
                              dash.page_container
                          ],
                          
                          
                          style = {'border':'2px solid yellow',
                                   
                                    'height':'2000px',

                                    'margin-left':'0px',
                                     
                                     'backgroundColor':'white'
                                     #'width':'500px',
                                     }
                      )
    ],
    
    style = {'height':'1900px',
             
            'backgroundColor':'white',

             #'background': 'radial-gradient(circle at 81.9% 53.5%, rgba(173, 53, 53, 0.9) 16.3%, rgba(240, 60, 60, 0.9) 100.2%)',
             'background-blur': '5px'
            }
)









app.layout = dbc.Container([row_1,row_2],
                           
                           fluid=True, 
                           
                           style={'border': '5px solid black',
                                  
                                  'height':'2105px',
                          
                          })


@app.callback(
        

    Output("offcanvas", "is_open"),


    Input("open-offcanvas-button", "n_clicks"),


    [State("offcanvas", "is_open")],


)
def toggle_offcanvas(n_clicks, is_open):


    if n_clicks:
        return not is_open
    return is_open




@app.callback(
    Output("image-display", "src"),
    Input("interval-component", "n_intervals")
)
def update_image(n):
    # Calculate the index of the next image to display
    image_index = n % len(image_urls)
    asset_url = dash.get_asset_url(image_urls[image_index])
    
    return asset_url






if __name__ == "__main__":
    app.run_server(debug=True)





