









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
from plotly.subplots import make_subplots

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
print(df['created_year'].dtype)
df['Year'] = pd.to_datetime(df['created_year'], format='%Y', errors='coerce')
df['Year'] = pd.to_numeric(df['Year'].dt.year, errors='coerce').astype(pd.Int64Dtype())
df['subscribers_for_last_30_days'] = pd.to_numeric(df['subscribers_for_last_30_days'], errors='coerce')
df['video_views_for_the_last_30_days'] = pd.to_numeric(df['video_views_for_the_last_30_days'], errors='coerce')

# df['Year'] = df['Year'].astype(str)
df = df[df['Year'] != 1970]

# df['created_year'] = pd.to_datetime(df['created_year'], format='%Y')
# df['Year'] = df['created_year'].apply(lambda x: x.strftime('%Y'))
df.dropna(inplace=True)




counts = [df[df['Country'] == x].shape[0] for x in df['Country'].unique()]
country_names = df['Country'].unique()

# Combine country names and counts, then sort by counts in descending order
sorted_data = sorted(zip(country_names, counts), key=lambda x: x[1], reverse=True)[:10]

# Extract the top 10 country names and counts
top_10_countries = [country for country, count in sorted_data]
top_10_counts = [count for country, count in sorted_data]







bar_colors = ['mediumaquamarine', 'royalblue', 'coral', 'gold', 'purple',
              'pink', 'cyan', 'magenta', 'lime', 'brown']



#page 1 figure 1 ------------------


fig = make_subplots(rows=1, cols=1)

# Add the bar trace to the subplot
trace = go.Bar(x=top_10_countries, y=top_10_counts, text=top_10_counts, textposition='outside',marker=dict(color=bar_colors))
fig.add_trace(trace)

# Update layout
fig.update_layout(
    title="Top 10 Countries by Count",
    xaxis_title="Country",
    yaxis_title="Count",
    width=750, 
    height=550,
      paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)'
)

# Show the plot



#page 1 figure 1 ------------------



# page 1 figure 2 -------------
counts = [df[df['channel_type'] == x].shape[0] for x in df['channel_type'].unique()]
channel_types = df['channel_type'].unique()

# Combine country names and counts, then sort by counts in descending order
sorted_data = sorted(zip(channel_types, counts), key=lambda x: x[1], reverse=True)[:10]

# Extract the top 10 country names and counts
top_10_channel_type = [channel_type for channel_type, count in sorted_data]
top_10_counts = [count for channel_type, count in sorted_data]


fig2 = make_subplots(rows=1, cols=1)

# Add the bar trace to the subplot
trace = go.Bar(x=top_10_channel_type, y=top_10_counts, text=top_10_counts, textposition='outside',marker=dict(color=bar_colors))
fig2.add_trace(trace)

# Update layout
fig2.update_layout(
    title="Top 10 Channel Type by Count",
    xaxis_title="Channel Type",
    yaxis_title="Count",
     width=750, 
    height=550,
      paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)'
)




#page 1 figure 3 -------------

# trace = go.Scatter(
#     x=sorted(df['Year'].unique()),
#     y=[df[df['Year']==f'{x}'].shape[0] for x in sorted(df['Year'].unique())],
#     mode='lines+markers',  # Show both lines and markers
#     marker=dict(size=8),  # Adjust the marker size as needed
# )

# # Create a layout for the chart
# layout = go.Layout(
#     title='Channel Created  Over Time',
#     xaxis=dict(title='Year'),
#     yaxis=dict(title='Count'),
# )

# # Create a figure and add the trace and layout
# fig3 = go.Figure(data=[trace], layout=layout)


fig3 = go.Figure(data=[go.Pie(labels=df[['subscribers','Youtuber']][['subscribers','Youtuber']].sort_values(by = 'subscribers',ascending= False).head(10)['Youtuber'],
 values=df[['subscribers','Youtuber']][['subscribers','Youtuber']].sort_values(by = 'subscribers',ascending= False).head(10)['subscribers'], hole=0.5 )])

# Customize the layout (optional)
fig3.update_layout(title='Top Youtuber Based on Subscribers')














#fig4--------------
df['subscribers_for_last_30_days'] = pd.to_numeric(df['subscribers_for_last_30_days'], errors='coerce')

# Group the data by 'channel_type' and calculate the sum of subscribers for each category
grouped_data = df.groupby(['channel_type', 'Country'])['subscribers_for_last_30_days'].sum().reset_index()

# Create a stacked bar chart
fig4 = go.Figure()

for channel_type in grouped_data['channel_type'].unique():
    filtered_data = grouped_data[grouped_data['channel_type'] == channel_type]
    fig4.add_trace(go.Bar(x=filtered_data['Country'], y=filtered_data['subscribers_for_last_30_days'], name=channel_type))

fig4.update_layout(barmode='stack', title='Stacked Bar Chart Example',
height = 600,paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)')

# Edit the x-axis labels
fig4.update_xaxes(
    tickvals=list(range(len(grouped_data['Country'].unique()))),
    ticktext=grouped_data['Country'].unique(),
    title_text='Country',  # Edit the x-axis title
      tickangle=45
)

# Show the stacked bar chart














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












#worldmap------

fig6 = go.Figure(go.Scattermapbox(
    lat=df['Latitude'],
    lon=df['Longitude'],
    mode='markers',
    marker=dict(size=10, color='blue'),
   # text=df['Location'],
))

# Set the layout for the map
fig6.update_layout(
    mapbox=dict(
       # accesstoken='',  # Replace with your Mapbox access token
        style='open-street-map',  # Map style
       # center=dict(lat=df['Latitude'].mean(), lon=df['Longitude'].mean()),  # Center of the map
        zoom=4,
          # Initial zoom level
    ),
    height = 900
)

# Show the map




#page 1 fig 6----

fdf = df[['Youtuber','lowest_monthly_earnings','channel_type']].sort_values(by='lowest_monthly_earnings',ascending = False).groupby(by=['channel_type']).sum().reset_index()






fig7 = make_subplots(rows=1, cols=1)

# Add the bar trace to the subplot
trace = go.Bar(x=fdf['channel_type'], y=fdf['lowest_monthly_earnings'], text=fdf['lowest_monthly_earnings'], textposition='outside',marker=dict(color=bar_colors))
fig7.add_trace(trace)

# Update layout
fig7.update_layout(
    title="Top 10 Countries by Count",
    xaxis_title="Country",
    yaxis_title="Count",
    width=950, 
    height=550,
      paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)'
)




# page 1 figure 8 -------
fig8 = make_subplots(rows=1, cols=1)

# Add the bar trace to the subplot
trace = go.Bar(x=df['category'], y=df['subscribers_for_last_30_days'], text=df['subscribers_for_last_30_days'], textposition='outside',marker=dict(color='red'))
fig8.add_trace(trace)

# Update layout
fig8.update_layout(
    title="Top 10 Countries by Count",
    xaxis_title="Country",
    yaxis_title="Count",
    width=950, 
    height=550,
      paper_bgcolor='rgba(0, 0, 0, 0)',
      plot_bgcolor = 'rgba(0, 0, 0, 0)'
)


















#start making interective graph .......


# filterd_df = df[(df['Country']=='India') & (df['Year']>=2017) & (df['Year']<=2018) ]

# print(filterd_df)


def pg1(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['video views'].sum().reset_index()
    figure1 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['video views'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure1.update_layout(title='<b>Category Wise Views</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure1

def pg2(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['uploads'].sum().reset_index()
    figure2 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['uploads'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure2.update_layout(title='<b>Categories wise uploads</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure2   



def pg3(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['lowest_monthly_earnings'].sum().reset_index()
    figure3 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['lowest_monthly_earnings'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure3.update_layout(title='<b>Lowest Monthly Earnings</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure3   




def pg4(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['highest_monthly_earnings'].sum().reset_index()
    figure4 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['highest_monthly_earnings'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure4.update_layout(title='<b>Highest Monthly Earnings</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure4       

def pg5(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['subscribers_for_last_30_days'].sum().reset_index()
    figure5 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['subscribers_for_last_30_days'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure5.update_layout(title='<b>Subscribers</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure5   




def pg6(filtered_df):
    filtered_df=filtered_df.groupby(by = 'category')['video_views_for_the_last_30_days'].sum().reset_index()
    figure6 = go.Figure(data=go.Bar(x= filtered_df['category'], y=filtered_df['video_views_for_the_last_30_days'],
                                    orientation='v', marker=dict(color='mediumaquamarine'),#dict(color=color_list)
                                     # text= [filtered_df[filtered_df['stage']==x].shape[0] for x in filtered_df['stage'].unique()],
                                      textposition='inside'))
    figure6.update_layout(title='<b>video views for the last 30 days</b>', xaxis_title='<b>Counts</b>', yaxis_title='<b>Categories</b>',
                      margin=dict(l=1, r=10, t=75,b=1),
                      xaxis=dict(
        #title='X-axis Title',
        title_standoff=5,
        tickangle=40
    ),plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)'),
    return figure6 




