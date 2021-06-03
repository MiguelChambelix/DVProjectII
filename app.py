import plotly.graph_objects as go  # We are only importing the 'graph_objects' module from plotly here
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly import tools
import plotly.express as px
from skimage import io
from datetime import date
from datetime import datetime


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
############################################# MAIN TITLE ##############################################
    html.Div([
    html.H1(['CRYPTO CURRENCIES COMPARISON'], style={'padding' : 20, 'text-align':'center', 'font-family':'Verdana','backgroundColor': '#0B3954', 'color': 'white'})
    ]),
##################################### CRYPTO SELECTION ################################################
html.Div([
    html.Div([
        html.Div([dcc.Graph(id='Image1')],style={'margin-left' : '5%','margin-right' : 'auto','backgroundColor': 'white' }),

        html.Div([
        html.H2(["Select the Currencies to compare"], style={'text-align':'center', 'font-family':'Verdana','margin-top' : '10%','margin-bottom' : '15%'}),

        html.Div([
        html.Div([
            dcc.Dropdown(
                id='crypto_drop1',
                options=crypto_list,
                value = 'ETH',
                multi=False,
                clearable=False,
                placeholder="Select a Currency")], style={'width': '30%','height' : '30%' ,'margin-left' : '10%','margin-right' : 'auto','font-family':'Verdana' }),
        html.Div([
            dcc.Dropdown(
                id='crypto_drop2',
                options=crypto_list,
                value = 'BTC',
                multi=False,
                clearable=False,
                placeholder="Select a Currency")],
            style={'width': '30%','height' : '30%' ,'margin-left' : 'auto','margin-right' : '10%','font-family':'Verdana' })
        ], style={'width': "100%", 'display': 'flex'}, className='box')]),


        html.Div([dcc.Graph(id='Image2')],style={'margin-left' : 'auto','margin-right' : '5%','backgroundColor': 'white' })
    ], style={'display' : 'flex', 'backgroundColor': 'white'}),


], style={'width': '100%','height' : '20%'}),

######################################## TABLES AND RADAR #############################################

    html.Div([
        html.Div([
        dcc.Graph(id='Table1')], style={'width':'25%', 'display': 'flex','margin-left' : '1%','margin-right' : 'auto','font-family':'Verdana' }, className='box'),

        html.Div([
        dcc.Graph(id='radar_chart')], style={'width':'50%', 'display': 'flex','font-family':'Verdana' }, className='box'),

        html.Div([
        dcc.Graph(id='Table2')], style={'width':'25%', 'display': 'flex','margin-left' : 'auto','margin-right' : '5%','font-family':'Verdana' }, className='box')],

        style={'width': "100%", 'height':'20%', 'display': 'flex','margin-left' : '5%','margin-right' : '5%','margin-top' : '3%','margin-bottom' : '1%','backgroundColor': 'white'}, className='box'),

######################################## INVESTMENT ANALYSIS ###########################################

        html.Br(),
        html.H2(["Investment Analysis"], style={'text-align':'center', 'font-family':'Verdana','margin-top' : '2%','margin-bottom' : '2%'}),

######################################## INVESTMENT VALUES #############################################
        html.Div([

            html.Div([
                dcc.Graph(id='scorecard1')], style={'width':'20%' , 'display': 'flex', 'font-family': 'Verdana','margin-left' : '2%'},
                className='box'),

            html.Div([

            html.Label(['Investment Value'], style = {'text-align':'center'}),
            html.Br(),
            html.Label(['USD ($)'], style={'text-align': 'center', 'fontSize': 10}),
            html.Br(),
            html.Br(),
            dcc.Input(
                id="invest_value".format('number'),
                value= 1,
                type='number',

                placeholder="Insert Value to invest".format('number'),
                style = {'height': 40, 'fontSize': 18, 'text-align':'center'}
            )], style={'width':'25%', 'height': '100%','margin-left' : '2%','margin-right' : '2%', 'text-align':'center'}),

            html.Button('CALCULATE', id='submit-val', n_clicks=0, style = {'width':100,'height': 40, 'margin-top' : '2%',
                                                                           'font-family': 'Verdana'}),


            html.Div([
            html.Label(['Investment Date'], style = {'text-align':'center'}),
            html.Br(),
            html.Label(['(YYYY-MM-DD)'], style = {'text-align':'center','fontSize': 10}),
            html.Br(),
            html.Br(),
            dcc.Input(
                id='invest_date',
                type='text',
                value='2021-01-01',
                style={'height': 40, 'fontSize': 18, 'text-align':'center'},


            )], style={'width':'25%' ,'height': '100%','margin-left' : '2%','margin-right' : '2%','text-align':'center'}),


            html.Div([
                dcc.Graph(id='scorecard2')], style={'width':'20%' ,'display': 'flex', 'font-family': 'Verdana','margin-left' : '2%','margin-right' : '1%'},
                className='box'),

    ], style={'display':'flex', 'height':'100%','margin-left' : '5%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%','font-family':'Verdana'}),

    html.Br(),

######################################## LINE CHART SETTINGS #############################################

    html.Div([
     html.Div([
        html.Label('X - AXIS SETTINGS'),

        dcc.RadioItems(
            id='lin_log',
            options=[dict(label='LINEAR', value='linear'), dict(label='LOG', value='log')],
            value='linear',
            style={'margin-top' : '5%','height':40}
        )], style={'text-align':'center','height': '100%', 'width':'20%','margin-left' : '1%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%','font-family':'Verdana' }),


     html.Div([
        html.Label('DATA SETTINGS'),

        dcc.RadioItems(
            id='daily_change',
            options=[dict(label='Profit', value='Profit ($)'), dict(label='Daily Change', value='Daily Change (%)'),dict(label='Daily Value', value='Closing Price (USD)')],
            value='Profit ($)',
            style={'margin-top' : '5%','height':40}
        )], style={'text-align':'center','height': '100%', 'width':'30%','margin-left' : '1%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%','font-family':'Verdana'}),

    html.Div([
        html.Label('DATE RANGE'),
        html.Div([

            dcc.RangeSlider(
                id='date_range',
                marks={i: '{}'.format(i) for i in range(2014, 2022)},
                min=2014,
                max=2021,
                #type = 'value',
                value=[2020, 2021]
            )], style={'height':40,'font-family':'Verdana','padding':'2%' })

        ], style={'text-align':'center','height': '100%', 'width':'30%','margin-left' : '1%','margin-right' : '5%','backgroundColor': '#F5F3F6','padding':'1%','font-family':'Verdana' })

     ], style={'display':'flex','margin-left' : '15%','margin-right' : '5%'}),

######################################## LINE CHART #############################################

    dcc.Graph(id='line_chart')


], style={'backgroundColor': 'white'}) #gray color


@app.callback(
    [

    Output('line_chart', 'figure'),
    Output('radar_chart', 'figure'),
    Output('Table1', 'figure'),
    Output('Table2', 'figure'),
    Output('Image1', 'figure'),
    Output('Image2', 'figure'),
    Output('scorecard1', 'figure'),
    Output('scorecard2', 'figure')

    ],
    [
    Input('crypto_drop1', 'value'),
    Input('crypto_drop2', 'value'),
    Input('submit-val', 'n_clicks'),
    Input("lin_log", "value"),
    Input("daily_change", "value"),
    Input("date_range", "value"),
    #Input("date_range", "end_date")
    ],
    [
    State('invest_value', 'value'),
    State('invest_date', 'value')
    ]
)
def update_graph(crypto1, crypto2,n ,lin_log, data_type, picked_date, invest_value, invest_date):#, picked_end_date):

    invest_date = datetime.strptime(invest_date, '%Y-%m-%d')

    picked_start_date = pd.to_datetime(str(picked_date[0])+"-01-01")  #date(2014,1,1)#date(picked_date[0],1,1)
    if str(picked_date[1]) == '2021':
        picked_end_date = pd.to_datetime(str(picked_date[1]) + "-05-26")
    else:
        picked_end_date = pd.to_datetime(str(picked_date[1])+"-12-01") #date(picked_date[1],12,31)

    ######################################## AUX COLUMNS FOR PROFIT #############################################

    cryptoprice_1 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]

    cryptonumber_1 = invest_value / cryptoprice_1

    cryptoprice_2 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]

    cryptonumber_2 = invest_value / cryptoprice_2

    prices["Profit 1"] = prices[prices["Currency"] == crypto1]["Closing Price (USD)"].apply(lambda line: line * cryptonumber_1)
    prices["Profit 2"] = prices[prices["Currency"] == crypto2]["Closing Price (USD)"].apply(lambda line: line * cryptonumber_2)

    prices["Profit 1"] = prices["Profit 1"].fillna(0)
    prices["Profit 2"] = prices["Profit 2"].fillna(0)

    prices["Profit ($)"] = prices["Profit 1"] + prices["Profit 2"]

    ######################################## LINE CHART #############################################

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
    max_crypto1 = max(prices_dates[prices_dates["Currency"]==crypto1][data_type])

    max_date_crypto1 = list(prices_dates[(prices_dates["Currency"] == crypto1) & (prices_dates[data_type] == max_crypto1)]["Date"])[0]

    filtered_currency2 = prices_dates[prices_dates['Currency'] == crypto2]

    temp_data2 = dict(
        type='scatter',
        y=filtered_currency2[data_type],
        x=filtered_currency2['Date'],
        name=crypto2,
        line=dict(color="#9CD3CD")
    )
    max_crypto2 = max(prices_dates[prices_dates["Currency"]==crypto2][data_type])

    max_date_crypto2 = list(prices_dates[(prices_dates["Currency"] == crypto2) & (prices_dates[data_type] == max_crypto2)]["Date"])[0]

    max_crypto = max([max_crypto1, max_crypto2])

    line_data = [temp_data1, temp_data2]

    line_layout = dict(xaxis=dict(title='Date'),
                       yaxis=dict(title= data_type + "(" + lin_log + ")" ),
                       title = data_type + " for " + list(currencies[currencies["Currency"]==crypto1]["Name"])[0] + " vs " + list(currencies[currencies["Currency"]==crypto2]["Name"])[0],
                       plot_bgcolor='white',
                       )

    fig_line_chart = go.Figure(data=line_data, layout=line_layout)
    fig_line_chart.update_yaxes(type=lin_log)
    fig_line_chart.update_layout(hovermode="x")
    fig_line_chart.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left",  x=0.01))
    fig_line_chart.update_xaxes(ticklabelmode="period", dtick="M1", tickformat="%b\n%Y")
    fig_line_chart.add_annotation(bgcolor="#F5F3F6", opacity=0.95, y=max_crypto1, x=max_date_crypto1, text=("Max "+ data_type + " for " + crypto1 + " : " + str(round(max_crypto1,2))) ,showarrow=True,arrowhead=1)
    fig_line_chart.add_annotation(bgcolor="#F5F3F6", opacity=0.95, y=max_crypto2, x=max_date_crypto2, text=("Max "+ data_type + " for " + crypto2+ " : " + str(round(max_crypto2,2))), showarrow=True,arrowhead=1)

    if lin_log == "linear":
        fig_line_chart.add_shape(type="line", x0=invest_date, y0=0, x1=invest_date, y1=max_crypto,
                                 line=dict(color="red", width=2, dash="dot"))
        fig_line_chart.add_trace(go.Scatter(name="Investment Date",x=[invest_date],y=[max_crypto], marker=dict(color=["red"]),mode='markers'))

    else:
        pass
    ######################################## RADAR CHART ##################################################

    radar_data = []

    categories = list(attributes["Attribute"].unique())

    radar_data1 = go.Scatterpolar(
        r=attributes[attributes["Currency"] == crypto1]["Amount"],
        theta=categories,
        fill='toself',
        name= crypto1,
        line=dict(color="#0B3954"),
        text= attributes[attributes["Currency"] == crypto1]["Description"]
    )

    radar_data2 = go.Scatterpolar(
        r=attributes[attributes["Currency"] == crypto2]["Amount"],
        theta=categories,
        fill='toself',
        name=crypto2,
        line=dict(color="#9CD3CD"),
        text= attributes[attributes["Currency"] == crypto2]["Description"]
    )

    radar_layout = dict(polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]

        )),
        showlegend=True,
        margin=dict(l=10, r=10, b=10, t=30),
        #title = crypto1 + " vs " + crypto2 + " Main Stats"

    )

    radar_data = [radar_data1, radar_data2]

    fig_radar_chart = go.Figure(data=radar_data, layout=radar_layout )
    fig_radar_chart.update_annotations(width = 40)
    fig_radar_chart.update_layout(legend=dict(yanchor="top", y=1, xanchor="right", x=0.85, orientation="v"))
    #fig_radar_chart.update_layout(title={'y': 0.99,'x': 0.2,'xanchor': 'center','yanchor': 'top'})


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

    layout_table1 = dict(width = 300, margin=dict(l=10, r=10, b=10, t=10))

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

    layout_table2 = dict(width = 300, margin=dict(l=10, r=10, b=10, t=10))

    table2 = go.Figure(data=table2_data, layout=layout_table2)

    #################### IMAGE 1 CHART #########################
    img1 = io.imread(list(pictures[pictures["Currency"]== crypto1]["Picture"])[0])
    image1 = px.imshow(img1)
    image1.update_xaxes(showticklabels=False)
    image1.update_yaxes(showticklabels=False)
    image1.update_layout(width=200, height=200, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor = 'white')


    #################### IMAGE 2 CHART #########################
    img2 = io.imread(list(pictures[pictures["Currency"] == crypto2]["Picture"])[0])
    image2 = px.imshow(img2)
    image2.update_xaxes(showticklabels=False)
    image2.update_yaxes(showticklabels=False)
    image2.update_layout(width=200, height=200, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor = 'white')

    #################### SCORECARD 1 CHART #########################
    cryptoprice1 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]

    cryptonumber1 = invest_value / cryptoprice1

    crypto_lastprice1 = list(prices[(prices["Date"] == '26/05/2021') & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]

    profit1 = (cryptonumber1 * crypto_lastprice1) - (cryptonumber1 * cryptoprice1)

    scorecard1 = go.Figure(go.Indicator(
        mode="number+delta",
        value=round(float(profit1), 2),
        number={'prefix': "$"},
        delta={'position': "bottom", 'reference': invest_value, 'relative' :True},
    ))
    scorecard1.update_layout(width=200, height=100, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor='rgba(0,0,0,0)')

    #################### SCORECARD 2 CHART #########################
    cryptoprice2 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]

    cryptonumber2 = invest_value / cryptoprice2

    crypto_lastprice2 = list(prices[(prices["Date"] == '26/05/2021') & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]

    profit2 = (cryptonumber2 * crypto_lastprice2) - (cryptonumber2 * cryptoprice2)

    scorecard2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=round(float(profit2), 2),
        number={'prefix': "$"},
        delta={'position': "bottom", 'reference': invest_value, 'relative' :True},
    ))
    scorecard2.update_layout(width=200, height=100, margin=dict(l=10, r=10, b=10, t=10), plot_bgcolor='rgba(0,0,0,0)')

    return fig_line_chart, \
           fig_radar_chart, \
           table1, \
           table2, \
           image1, \
           image2, \
           scorecard1, \
           scorecard2


if __name__ == '__main__':
    app.run_server(debug=True)
