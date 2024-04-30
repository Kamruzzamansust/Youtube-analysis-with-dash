
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import dash
#import dash_canvas
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd 
import style as st
from plotly.subplots import make_subplots
import graphs



dash.register_page(__name__,path = '/', name = 'Home')

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




















def crdf(x,y):
     s=dbc.Card(
            dbc.CardBody([
            html.H4(f'{x}', className="card-title",style = {'text-align':'center'}),
            html.H2(f'{y}',style = {'text-align':'center'})
            #html.P("This is some card content. You can put whatever you like here.", className="card-text"),
            #dbc.Button("Click me", color="primary"),
        ]),
         style = st.card_style # Adjust the card width as needed
    )
     return s 



#fig5
trace = go.Scatter(
    x=sorted(df['Year'].unique()),
    y=[df[df['Year']==f'{x}'].shape[0] for x in sorted(df['Year'].unique())],
    mode='lines+markers',  # Show both lines and markers
    marker=dict(size=8),  # Adjust the marker size as needed
)

# Create a layout for the chart
layout = go.Layout(
    title='Channel Created  Over Time',
    xaxis=dict(title='Year'),
    yaxis=dict(title='Count'),
    paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)'
)

# Create a figure and add the trace and layout
fig5 = go.Figure(data=[trace], layout=layout)






row_1 = dbc.Row(
    [
        dbc.Col(
            [
            dbc.Card(
            dbc.CardBody([
            html.H4("Total Observation", className="card-title",style = {'text-align':'center'}),
            
            html.H2(df.shape[0],style = {'text-align':'center',
                                         'margin-top':'15px'})


        ]),
        style={"width": "400px",
               'height':'190px',
               'margin-top':'10px',
               'border':'3px solid black',
               'boxShadow': '5px 5px 5px grey'}  # Adjust the card width as needed
    )
            ]
        ),






        dbc.Col(
            [
             crdf('Total Country',df['Country'].nunique()),
             
            ]
        ),





         dbc.Col(
            [
             crdf('Total Channel Type',df['channel_type'].nunique())
            ]
        ),




         dbc.Col(
            [
             crdf('Unique Category',df['category'].nunique())
            ]
        ),





    ],style ={'height':'210px',
              #'backgroundColor':'white'
              }
)





row_2 = dbc.Row(
     [
          dbc.Col(
               [
                    dcc.Graph(id='top-10-country-by-frquency',figure =graphs.fig )

               ],style = {
                          'border':'4px solid red',
                          'margin-right':'10px',
                          'border-radius':'10px',
                          'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                            'boxShadow': '5px 5px 5px grey'}
          ),
           dbc.Col(
               [
                    dcc.Graph(id='top-10-channel_type' ,figure =graphs.fig2)

                    
               ],style = {#'backgroundColor':'white',
                          'border':'4px solid red',
                           'border-radius':'10px',
                            'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                              'boxShadow': '5px 5px 5px grey'}
          ),
           dbc.Col(
               [
                    dcc.Graph(id='channel creation obver the year' ,figure =graphs.fig3)
               ],style = {#'backgroundColor':'white',
                          'border':'4px solid red',
                        'margin-left':'10px',
                         'border-radius':'10px',
                           'boxShadow': '5px 5px 5px grey'}
          ),
     ],style = {#'backgroundColor':'black',
                'height':'500px',
                'margin-top':'20px',
                 'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                  }
)



row_3 = dbc.Row(
     [
          dbc.Col(
               [
                    dcc.Graph(id='stack-bar plot',figure =graphs.fig4 )

               ],width = 8 , style = { 'margin-top':'50px',
                          'border':'4px solid red',
                          'margin-right':'10px',
                          'border-radius':'10px',
                          'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                            'boxShadow': '5px 5px 5px grey'}
          ),
           dbc.Col(
               [
                    dcc.Graph(id='line-plot',figure =fig5 )

               ],style = { 'margin-top':'50px',
                          'border':'4px solid red',
                          'margin-right':'10px',
                          'border-radius':'10px',
                          'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                            'boxShadow': '5px 5px 5px grey'}
          ),
  

     ],style = {#'backgroundColor':'black',
                'height':'600px',
                'margin-top':'20px',
                 'background': 'linear-gradient(rgba(255, 255, 255, 0)'}
)


row_4 = dbc.Row(
    [
        dbc.Col(
            [
                dcc.Graph(id= 'lowest_earning_lastmonth', figure = graphs.fig7)
            ],style = { 'margin-top':'20px',
                          'border':'4px solid red',
                          'margin-right':'10px',
                          'border-radius':'10px',
                          'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                            'boxShadow': '5px 5px 5px grey'}
        ),
         dbc.Col(
            [
                 dcc.Graph(id= 'subsciber count by category', figure = graphs.fig8)
            ],style = { 'margin-top':'20px',
                          'border':'4px solid red',
                          'margin-right':'10px',
                          'border-radius':'10px',
                          'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                            'boxShadow': '5px 5px 5px grey'}
        ),
      
    ],style = {#'backgroundColor':'black',
                'height':'600px',
                'margin-top':'50px',
                 'background': 'linear-gradient(rgba(255, 255, 255, 0)'}
)









layout=dbc.Container(
    [
        row_1,
        row_2,
        row_3,
        row_4

    ],fluid=True, style={
         
         'height':'1000px'
        ,'border':'0px solid black',
                          
                          }
)