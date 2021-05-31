import plotly.graph_objects as go  # We are only importing the 'graph_objects' module from plotly here
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly import tools
import plotly.express as px
from skimage import io
from datetime import date

currencies = pd.read_excel("Currencies.xlsx", "Currency",
                           engine='openpyxl')
prices = pd.read_excel("Currencies.xlsx", "Prices",
                       engine='openpyxl')
attributes = pd.read_excel("Currencies.xlsx", "Attribute",
                           engine='openpyxl')
pros = pd.read_excel("Currencies.xlsx", "Description",
                     engine='openpyxl')
pictures = pd.read_excel("Currencies.xlsx", "Pictures",
                         engine='openpyxl')

# # Create First Line Chart
#
# layout_line = dict(
#     title=dict(
#         text='Crypto Over Time',
#         x=.5
#         # This parameter puts the title text in a position from 0 to 1 acording to the x axis, i.e x=.5 is a centered title
#     ),
#     xaxis=dict(
#         title='X Axis'
#     ),
#     yaxis=dict(
#         title='Y Axis',
#         range=(0, 80000)
#     ),
#     height=800,
#     width=1500,
#     paper_bgcolor='azure'
# )
#
# data_line1 = dict(type='scatter',
#                   x=prices[prices["Currency"] == "BTC"]['Date'],
#                   y=prices[prices["Currency"] == "BTC"]['Closing Price (USD)'],
#                   name='BTC'
#                   )
#
# data_line2 = dict(type='scatter',
#                   x=prices[prices["Currency"] == "ETH"]['Date'],
#                   y=prices[prices["Currency"] == "ETH"]['Closing Price (USD)'],
#                   name='ETH'
#                   )
#
# data_line = [data_line1, data_line2]
#
# lineChart = go.Figure(data=data_line, layout=layout_line)
#
# # lineChart.show()
#
#
# # Create Tables
#
# layout_table = dict(width=800, height=500)
#
# data_table1 = go.Table(header=dict(values=['Description'],
#                                    line_color='darkslategray',
#                                    fill_color='lightskyblue',
#                                    align='left'),
#
#                        cells=dict(values=[pros[pros["Currency"] == "BTC"]["Description"]  # 1st column
#                                           ],  # 2nd column
#                                   line_color='darkslategray',
#                                   fill_color='lightcyan',
#                                   align='left'))
#
# table1 = go.Figure(data=data_table1, layout=layout_table)
#
# # table1.show()
#
# data_table2 = go.Table(header=dict(values=['Description'],
#                                    line_color='darkslategray',
#                                    fill_color='lightskyblue',
#                                    align='left'),
#
#                        cells=dict(values=[pros[pros["Currency"] == "ETH"]["Description"]  # 1st column
#                                           ],  # 2nd column
#                                   line_color='darkslategray',
#                                   fill_color='lightcyan',
#                                   align='left'))
#
# table2 = go.Figure(data=data_table2, layout=layout_table)
#
# # table2.show()
#
# categories = list(attributes["Attribute"].unique())
#
# # Create Radar
#
# data_radar1 = go.Scatterpolar(
#     r=attributes[attributes["Currency"] == "BTC"]["Amount"],
#     theta=categories,
#     fill='toself',
#     name='BTC'
# )
#
# data_radar2 = go.Scatterpolar(
#     r=attributes[attributes["Currency"] == "ETH"]["Amount"],
#     theta=categories,
#     fill='toself',
#     name='ETH'
# )
#
# layout_radar = dict(polar=dict(
#     radialaxis=dict(
#         visible=False,
#         range=[0, 100]
#     )),
#     showlegend=False
# )
#
# data_radar = [data_radar1, data_radar2]
#
# radar = go.Figure(data=data_radar, layout=layout_radar)
#
# # radar.show()
#
#
# ##Create Sub Plot
#
# # the 'rowspan' option inside the 'specs' defines the amount of rows the graph object in that position will ocupy
# # Keep in mind that rows below and occupied should have 'None' as their value
# # Naturally there is an equivalent 'colspan' option
#
# titles = ['Crypto 1', 'Radar', 'Crypto 2', "", "Time Series"]  # It ignores None type positions in the specs matrix
#
# plot = make_subplots(rows=2,
#                      cols=3,
#                      subplot_titles=titles,
#                      specs=[[dict(type='table', rowspan=1), dict(type='polar'), dict(type='table', rowspan=1)],
#                             [dict(type='xy', colspan=3), {}, {}]]
#                      )
#
# # Both scatter and the bar type plots had several data traces, you need to add them iteratively
# # In their respective position in the subplot
# for i in range(len(data_line)):
#     plot.add_trace(data_line[i], row=2, col=1)
#
# for i in range(len(data_radar)):
#     plot.add_trace(data_radar[i], row=1, col=2)
#
# plot.add_trace(data_table1, row=1, col=1)
# plot.add_trace(data_table2, row=1, col=3)
#
# plot.update_layout(height=800, title_text="Crypto Comparison")
# # plot.show()


# Create Dash Options
crypto_options = currencies["Currency"]
crypto_list = []
for crypto in crypto_options:
    crypto_list.append({'label': crypto, 'value': crypto})

crypto_list
# The app itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([

    html.H1(['CRYPTO CURRENCIES COMPARISON'], style={'text-align':'center', 'font-family':'Verdana','backgroundColor': '#0B3954', 'color': 'white'}),

html.Div([
    html.Div([
        html.Div([dcc.Graph(id='Image1')],style={'margin-left' : '5%','margin-right' : 'auto','backgroundColor': 'white' }),
        html.Div([dcc.Graph(id='Image2')],style={'margin-left' : 'auto','margin-right' : '5%','backgroundColor': 'white' })
    ], style={'display' : 'flex', 'backgroundColor': 'white'}),

      html.Div([
        html.Div([
            dcc.Dropdown(
                id='crypto_drop1',
                options=crypto_list,
                value = 'ETH',
                multi=False,
                clearable=False,
                placeholder="Select a Currency")], style={'width': '10%','height' : '30%' ,'margin-left' : '10%','margin-right' : 'auto','font-family':'Verdana' }),
        html.Div([
            dcc.Dropdown(
                id='crypto_drop2',
                options=crypto_list,
                value = 'BTC',
                multi=False,
                clearable=False,
                placeholder="Select a Currency")],
            style={'width': '10%','height' : '30%' ,'margin-left' : 'auto','margin-right' : '10%','font-family':'Verdana' })
        ], style={'width': "100%", 'display': 'flex'}, className='box')
], style={'width': '100%','height' : '20%'}),

    html.Div([
        dcc.Graph(id='Table1'),

        dcc.Graph(id='radar_chart'),

        dcc.Graph(id='Table2')],
        style={'width': "100%", 'height':'30%', 'display': 'flex','margin-left' : '5%','margin-right' : '5%','margin-top' : '3%','margin-bottom' : '0','backgroundColor': 'white'}, className='box'),

   # html.Br(),  # paragrafo
    html.Div([
     html.Div([
        html.Label('X - AXIS SETTINGS:'),

        dcc.RadioItems(
            id='lin_log',
            options=[dict(label='linear', value='linear'), dict(label='log', value='log')],
            value='linear'
        )], style={'height': '100%','margin-left' : '5%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%'}),
     html.Div([
        html.Label('DATA SETTINGS:'),

        dcc.RadioItems(
            id='daily_change',
            options=[dict(label='Daily Value', value='Closing Price (USD)'), dict(label='Daily Change', value='Daily Change')],
            value='Closing Price (USD)'
        )], style={'height': '100%','margin-left' : '5%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%'}),

    html.Div([
        html.Label('DATE RANGE:'),
        html.Div([
            dcc.DatePickerRange(
                id='date_range',
                min_date_allowed=date(2013, 10, 1),
                max_date_allowed=date(2021, 5, 29),
                start_date=date(2018, 10, 1),
                end_date=date(2021, 5, 29),
                display_format='MMM Do, YY')], style={'height':'80%'})

        ], style={'height': '100%','margin-left' : '5%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%'})

     ], style={'display':'flex','margin-left' : '5%','margin-right' : '5%'}),

    dcc.Graph(id='line_chart')


], style={'backgroundColor': 'white'}) #gray color


@app.callback(
    [

    Output('line_chart', 'figure'),
    Output('radar_chart', 'figure'),
    Output('Table1', 'figure'),
    Output('Table2', 'figure'),
    Output('Image1', 'figure'),
    Output('Image2', 'figure')
    ],
    [
    Input('crypto_drop1', 'value'),
    Input('crypto_drop2', 'value'),
    Input("lin_log", "value"),
    Input("daily_change", "value"),
    Input("date_range", "start_date"),
    Input("date_range", "end_date")
    ]
)
def update_graph(crypto1, crypto2, lin_log, data_type, picked_start_date, picked_end_date):
    #################### LINE CHART #########################

    line_data = []

    prices_dates = prices[(prices["Date"]>= picked_start_date) & (prices["Date"]<= picked_end_date)]

    filtered_currency1 = prices_dates[prices_dates['Currency'] == crypto1]

    temp_data1 = dict(
        type='scatter',
        y=filtered_currency1[data_type],
        x=filtered_currency1['Date'],
        name=crypto1,
        line=dict(color="#0B3954")
    )


    filtered_currency2 = prices_dates[prices_dates['Currency'] == crypto2]

    temp_data2 = dict(
        type='scatter',
        y=filtered_currency2[data_type],
        x=filtered_currency2['Date'],
        name=crypto2,
        line=dict(color="#9CD3CD")
    )


    line_data = [temp_data1, temp_data2]

    line_layout = dict(xaxis=dict(title='Year'),
                       yaxis=dict(title="Closing Price (USD)"),
                       title = crypto1 + " vs " + crypto2,
                       plot_bgcolor='white',
                       )

    fig_line_chart = go.Figure(data=line_data, layout=line_layout)
    fig_line_chart.update_yaxes(type=lin_log)

    #################### RADAR CHART #########################

    radar_data = []

    categories = list(attributes["Attribute"].unique())

    radar_data1 = go.Scatterpolar(
        r=attributes[attributes["Currency"] == crypto1]["Amount"],
        theta=categories,
        fill='toself',
        name= crypto1,
        line=dict(color="#0B3954")
    )

    radar_data2 = go.Scatterpolar(
        r=attributes[attributes["Currency"] == crypto2]["Amount"],
        theta=categories,
        fill='toself',
        name=crypto2,
        line=dict(color="#9CD3CD")
    )

    radar_layout = dict(polar=dict(
        radialaxis=dict(
            visible=False,
            range=[0, 100]

        )),
        showlegend=False,
        margin=dict(l=0, r=10, b=10, t=0)
    )

    radar_data = [radar_data1, radar_data2]

    fig_radar_chart = go.Figure(data=radar_data, layout=radar_layout)


    #################### TABLE 1 CHART #########################
    table1_data = go.Table(header=dict(values=['Description' + " " + crypto1],
                         line_color='#0B3954',
                         fill_color='#0B3954',
                         font=dict(color='white', family="Verdana", size=12),
                         align='left'),

                         cells=dict(values=[pros[pros["Currency"]==crypto1]["Description"] # 1st column
                                           ], # 2nd column
                         line_color='#0B3954',
                         fill_color='#9CD3CD',
                         align='left'))

    layout_table1 = dict(width=300, height=400, margin=dict(l=10, r=10, b=10, t=10))

    table1 = go.Figure(data=table1_data, layout = layout_table1)

    #################### TABLE 2 CHART #########################
    table2_data = go.Table(header=dict(values=['Description' + " " + crypto2],
                                       line_color='#0B3954',
                                       fill_color='#0B3954',
                                       font=dict(color='white', family="Verdana", size=12),
                                       align='left'),

                           cells=dict(values=[pros[pros["Currency"] == crypto2]["Description"]  # 1st column
                                              ],  # 2nd column
                                      line_color='#0B3954',
                                      fill_color='#9CD3CD',
                                      align='left'))

    layout_table2 = dict(width=300, height=400, margin=dict(l=10, r=10, b=10, t=10))

    table2 = go.Figure(data=table2_data, layout=layout_table2)

    #################### IMAGE 1 CHART #########################
    img1 = io.imread(list(pictures[pictures["Currency"]== crypto1]["Picture"])[0])
    image1 = px.imshow(img1)
    image1.update_xaxes(showticklabels=False)
    image1.update_yaxes(showticklabels=False)
    image1.update_layout(width=300, height=300, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor = 'white')


    #################### IMAGE 2 CHART #########################
    img2 = io.imread(list(pictures[pictures["Currency"] == crypto2]["Picture"])[0])
    image2 = px.imshow(img2)
    image2.update_xaxes(showticklabels=False)
    image2.update_yaxes(showticklabels=False)
    image2.update_layout(width=300, height=300, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor = 'white')


    return fig_line_chart, \
           fig_radar_chart, \
           table1, \
           table2, \
           image1, \
           image2


if __name__ == '__main__':
    app.run_server(debug=True)
