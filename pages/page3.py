import pandas as pd 
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
from dash import html, dcc,Input,Output,State, callback,dash_table
import plotly.graph_objects as go
import dash
import graphs 
#import dash_canvas
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import dash_ag_grid as dag
dash.register_page(__name__, path = '/page-2', name =  'page2')





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
df['subscribers_for_last_30_days'] = pd.to_numeric(df['subscribers_for_last_30_days'], errors='coerce')
df['video_views_for_the_last_30_days'] = pd.to_numeric(df['video_views_for_the_last_30_days'], errors='coerce')

# df['Year'] = df['Year'].astype(str)
df = df[df['Year'] != 1970]

df.dropna(inplace=True)



print(df['Year'].min())




custom_marks = {
    2004:'2005',
    2006:'2006',
    2008:'2008',
    2010: '2010',
    2012: '2012',
    2014: '2014',
    2016: '2016',
    2018:'2018',
    2020 :'2020',
    2022 :'2022',# Add 2022 to the custom marks
}


row_1 = dbc.Row(
    [
        dbc.Col(
            [

            ]
        )
    ],style = {'backgroundColor':'gray',
    'height':'50px'}
)

row_2 = dbc.Row(
    [
        dbc.Col(
            [ 
              dbc.Row(
                
                [html.H3('Select Your Country'),
                                        dcc.Dropdown(
            id='Country-Dropdown',

             options=list(df['Country'].unique()) + ["ALL"], 
             value='ALL',  
             multi=False,
             style={'width': '300px',
                       'margin-top':'10px'})


                ],style = {'margin-top':'50px'}
              ),
              dbc.Row(
            #     [html.H3('Select Your Category'),
            #                                      dcc.Dropdown(
            # id='category-Dropdown',

            #  options=list(df['category'].unique()) + ["ALL"], 
            #  value='ALL',  
            #  multi=False, style={'width': '300px',
            #            'margin-top':'10px'})



            # ],style = {'margin-top':'120px'}
        ), 
        dbc.Row(
            [
                dcc.RangeSlider(
        id='year-slider',
       # marks={str(year): str(year) for year in df['Year']},
        min=int(df['Year'].min()),  # Convert to int
        max=int(df['Year'].max()),  # Convert to int
        step=5,
        value=[int(df['Year'].min()), int(df['Year'].max()),],
         marks=custom_marks,
         vertical= False
          # Convert to int
    ),
            ],justify = 'center',style = {'margin-top':'120px',
                                              'padding-left':'0px'}
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dcc.Markdown('''
    * YouTube is available in over 100 countries and supports more than 80 languages
    
    *  YouTube had over 2 billion logged-in monthly users.
    
    * The most-viewed video on YouTube was "Baby Shark Dance" by Pinkfong, with billions of views
    
    * Interact with your audience through comments and social media.
    
    * Collaborate with other YouTubers to expand your reach.
''')
            ]
        )


            ],width =3, style = {'backgroundColor':'#FFD384',
                                      'height':'1015px',
                                      'margin-top':'1px',
                                      #'position':'fixed'
                                      }
        ),
        dbc.Col(
            [
                dbc.Row(
                    [
                          dbc.Col(
                            [
                                dcc.Graph(id ='interective graph-1')

                            ],style = {'border':'4px solid red',
                             'border':'4px solid #FFD384',
                                             'margin-right':'10px',
                                              'margin-left':'10px',
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                          ),
                          dbc.Col(
                            [
                                dcc.Graph(id ='interective graph-2')

                            ] ,style = {'border':'4px solid red',
                             'border':'4px solid #FFD384',
                                             'margin-right':'10px',
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                        ),
                           dbc.Col(
                            [
                                dcc.Graph(id ='interective graph-3')

                            ] ,style = {'border':'4px solid #FFD384',
                             
                                             'margin-right':'10px',
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                        )
                    ],  
                    
                    style = {'height':'500px',
                    'backgroundColor':'white'}
                ),
                   dbc.Row(
                    [
                                dbc.Col(
                            [
                                  dcc.Graph(id ='interective graph-4')


                            ],  style = {'border':'4px solid #FFD384',
                             'border':'4px solid #FFD384',
                                             'margin-right':'10px',
                                             'margin-left':'10px',
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                          ),
                          dbc.Col(
                            [
                                dcc.Graph(id ='interective graph-5')


                            ],style = {'border':'4px solid #FFD384',
                             'border':'4px solid #FFD384',
                                             'margin-right':'10px',
                                             
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                        ),
                             dbc.Col(
                            [
                                dcc.Graph(id ='interective graph-6')

                            ],style = {      'border':'4px solid #FFD384',
                                             'margin-right':'10px',
                                            
                                             'border-radius':'10px',
                                             'background': 'linear-gradient(rgba(255, 255, 255, 0)',
                                             'boxShadow': '5px 5px 5px grey'}
                        )
                    ],style = { 'height':'500px',
                                'backgroundColor':'white',
                                'margin-top':'10px'}
                )
            ]
        )
        
    
       
    ],style ={'height':'1000px',
              'backgroundColor':'white',
             # 'position' :'fixed',
              }
)


row_3 = dbc.Row(
    [
        dbc.Col(
            [
                html.H5('Dash Ag Grid Table',style = {'text-align':'center'})
            ]
        )
    ],style = {'backgroundColor':'skyblue',
    'margin-top':'20px'}
)

row_4 = dbc.Row(
    [   
         dbc.Col(
        [
            dag.AgGrid(
            id = 'my-table',
            rowData = df.to_dict('records'),
            columnDefs = [{"field":i} for i in df.columns],
            defaultColDef = {'resizable':True,'sortable':True,'filter':True},
            style={'height': '800px'}

        ) 
        ]
    )
    ],style = {'height':'500px',
    'margin-top':'30px'}
    
    
)
# row_2 = dbc.Row(
#     [
#         dbc.Col(
#             [
#                dbc.Row(
#                 [
#                                         dcc.Dropdown(
#             id='Country-Dropdown',

#              options=list(df['Country'].unique()) + ["ALL"], 
#              value='ALL',  
#              multi=False,
#              style={'width': '300px',
#                        'margin-top':'10px'})


#                 ],style = {'margin-top':'50px',
#                 'backgroundColor':'white',
#                 }
#               ),
#               dbc.Row(
#                 [
#                                                  dcc.Dropdown(
#             id='category-Dropdown',

#              options=list(df['category'].unique()) + ["ALL"], 
#              value='ALL',  
#              multi=False, style={'width': '300px',
#                        'margin-top':'10px'})



#             ],style = {'margin-top':'50px',
#                 'backgroundColor':'white',
#                 }
#         ),
#         dbc.Row(
#             [
#                 dcc.RangeSlider(
#         id='year-slider',
#        # marks={str(year): str(year) for year in df['Year']},
#         min=int(df['Year'].min()),  # Convert to int
#         max=int(df['Year'].max()),  # Convert to int
#         step=5,
#         value=[int(df['Year'].min()), int(df['Year'].max()),],
#          marks=custom_marks,
#          vertical= False
#           # Convert to int
#     ),
#             ],justify = 'center',style = {'margin-top':'50px',
#                 'backgroundColor':'white',
#                 }
#         ) 
              
#             ],width = 3 ,style = {'height':'500px',
#             'backgroundColor':'white'}
#         ),
    
       
#     ]
# )









layout=dbc.Container([
    # row_1,
    row_2,
    row_3,
    row_4
]
        
    ,fluid=True, style={'height':'1065px',
                          'border':'2px solid black',
                          'backgroundColor':'white'
                          
                          }
)






@callback(
    Output('interective graph-1', 'figure'),
    Output('interective graph-2', 'figure'),
    Output('interective graph-3', 'figure'),
    Output('interective graph-4', 'figure'),
    Output('interective graph-5', 'figure'),
     Output('interective graph-6', 'figure'),

    Input('Country-Dropdown', 'value'),
    Input('year-slider', 'value'),
)
def update_bar_plot(selected_country, selected_years):
    if selected_country !='ALL':
        filtered_data = df[(df['Country'] == selected_country) &
                        (df['Year'] >= selected_years[0]) &
                        (df['Year'] <= selected_years[1])]
    else:
        filtered_data = df.copy()                    


    
      
    print(filtered_data)
    graph1 = graphs.pg1(filtered_data)  
    graph2 = graphs.pg2(filtered_data)
    graph3 = graphs.pg3(filtered_data)
    graph4 = graphs.pg4(filtered_data)
    graph5 = graphs.pg5(filtered_data)
    graph6 = graphs.pg6(filtered_data)

    return  graph1 ,graph2,graph3 ,graph4, graph5,graph6   
    

        