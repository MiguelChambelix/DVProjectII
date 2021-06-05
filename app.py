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

#Import Excel file with the data
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



# Create Dash Options for Dropdown
crypto_options = currencies["Currency"]
crypto_list = []
for crypto in crypto_options:
    crypto_list.append({'label': crypto, 'value': crypto})

# The app itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
############################################# MAIN TITLE ##############################################
    html.Div([
    html.H1(['CRYPTO CURRENCIES COMPARISON'], style={'width': '100%','padding' : 20, 'text-align':'center', 'font-family':'Verdana','backgroundColor': '#0B3954', 'color': 'white'}),
    html.Button('INFO', title = "This Dashboard was created with the purpose \n"
                                 "of comparing the hot topic regarding\n"
                                 "Cryptocurrencies and the main differences\n"
                                 "between them.\n"
                                 "\n"
                                 "The First section will help you understand\n"
                                 "the difference between the chosen currencies.\n"
                                 "\n"
                                 "The Second section tells you the story of \n"
                                 "investing in the cryptocurrency market and\n"
                                 "the possible profit that could have been made.\n"
                                 "\n"
                                 "Hovering the charts and buttons may show you\n"
                                 "tooltips related with the charts or data.",

                id='info', n_clicks=0, style = {'width':'3.5%','margin-top' : '0.5%','margin-left' : '2%','margin-right' : 'auto',
                                                                           'font-family': 'Verdana','backgroundColor': '#0B3954', 'color': 'white'})
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


        html.Div([dcc.Graph(id='Image2')],style={'margin-left' : 'auto','margin-right' : '10%','backgroundColor': 'white' })
    ], style={'display' : 'flex', 'backgroundColor': 'white'}),


], style={'width': '100%','height' : '20%'}),

    html.Div([
        html.Button('?', title="The Radar Chart contains the main stats \n"
                               "of the two Cryptocurrencies selected.\n"
                               "If you hover with your mouse the node for\n"
                               "each attribute you will be able to see a\n"
                               "description of what it is and the values\n"
                               "for the currency.\n"
                               "\n"
                               "In case you are not able to see the\n"
                               "description, click in the legend to\n"
                               "remove one of the currencies allowing\n"
                               "you to see only one currency at the time.\n",

                    id='info_radar', n_clicks=0, style={'font-family': 'Verdana', 'backgroundColor': 'white', 'color': 'black'})],
        style={'width': '3.5%', 'height': '2%', 'margin-top': '2%', 'margin-left': '35%', 'margin-right': 'auto'}),

    ######################################## TABLES AND RADAR #############################################

    html.Div([
        html.Div([
        dcc.Graph(id='Table1')], style={'width':'25%', 'display': 'flex','margin-left' : '1%','margin-right' : 'auto','font-family':'Verdana' }, className='box'),

    html.Div([
            dcc.Graph(id='radar_chart')], style={'width': '50%', 'display': 'flex', 'font-family': 'Verdana'},
            className='box'),

        html.Div([
        dcc.Graph(id='Table2')], style={'width':'25%', 'display': 'flex','margin-left' : 'auto','margin-right' : '5%','font-family':'Verdana' }, className='box')],

        style={'width': "100%", 'height':'20%', 'display': 'flex','margin-left' : '5%','margin-right' : '5%','margin-top' : '1%','margin-bottom' : '1%','backgroundColor': 'white'}, className='box'),

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

            html.Button('CALCULATE', id='submit-val', n_clicks=0, title= "The Calculation of the profit is based on\n"
                                                                         "the Amount Invested in the date selected.\n"
                                                                         "The formula uses the price of the currency\n"
                                                                         "on the date selected.\n"
                                                                         "\n"
                                                                         "It divides the invested amount by that price.\n"
                                                                         "This gives the number of currencies that you\n"
                                                                         "can buy on that date with that amount.\n"
                                                                         "\n"
                                                                         "Then it multiplies the number of currencies\n"
                                                                         "with the most recent price available of that\n"
                                                                         "currency, giving the total profit amount.\n"
                                                                         "\n"
                                                                         "The last day available is the 26th of May 2021.\n"
                                                                         "In case the invested date selected is before the\n"
                                                                         "first date available for the currency, it uses\n"
                                                                         "the first price available.",
            style = {'width':100,'height': 40, 'margin-top' : '2%', 'font-family': 'Verdana'}),


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

    dcc.ConfirmDialog(id='confirm', displayed =False, message = "\n"
                                                                "WARNING\n"
                                                                "\n"
                                                                "Investment Date is before the first available data\n"
                                                                "for one of the Currencies.\n"
                                                                "\n"
                                                                "Please select a new date for more accurate data.\n"
                                                                "\n"
                                                                "The calculation will be made based on the first\n"
                                                                "date available."),

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
        html.Div([
                html.Button('?', title="The Line Chart contains the values over \n"
                                       "time for of the two Cryptocurrencies selected.\n"
                                       "It shows by default the investment profit\n"
                                       "to tell you the story of what you could have\n"
                                       "gained/lost.\n"
                                       "\n"
                                       "You can also select the 'Daily Change'\n"
                                       "to analyse the volatility of each currency.\n"
                                       "\n"
                                       "The last option is the 'Daily Value' that\n"
                                       "shows the daily price of each currency.\n"
                                       "\n"
                                       "It is interesting to see that the profit may\n"
                                       "be very different from the daily value.\n"
                                       "\n"
                                       "A good example is the default option. It shows\n"
                                       "BTC, which is very well known and expensive,\n"
                                       "versus ETH, also well known but with a lower\n"
                                       "price.\n"
                                       "The interesting part is that although BTC has\n"
                                       "reached its maximum value recently, ETH is\n"
                                       "still much more profitable by far, with an\n"
                                       "investment in the beginning of 2021.\n"
                                       "This happens because what really matters\n"
                                       "is the gained percentage and not the real\n"
                                       "value of the currency.\n"
                                       "\n"
                                       "A currency that costs 10 000 USD and increases\n"
                                       "to 15 000 USD 'only' gained 50%, while a\n"
                                       "currency that costs 1 USD and increases\n"
                                       "to 2 USD gained 100%.",

                            id='info_line', n_clicks=0, style={'font-family': 'Verdana', 'backgroundColor': 'white', 'color': 'black'})],
                style={'width': '3.5%', 'height': '2%', 'margin-top': '0%', 'margin-left': '5%', 'margin-right': 'auto'}),

    dcc.Graph(id='line_chart'),

    html.Button('ABOUT THIS DASH', title = "This Dashboard was created by:\n"
                                           "Akvilina Akstinaite, m20200291\n"
                                           "Miguel Chambel, m20200326\n"
                                           "\n"
                                           "Sources: \n"
                                           "https://www.ig.com/en/cryptocurrency-trading/cryptocurrency-comparison \n"
                                           "https://coinmarketcap.com/",
                id='about', n_clicks=0, style = {'width':200,'height': 40, 'margin-top' : '2%','margin-left' : '5%','margin-right' : 'auto',
                                                                           'font-family': 'Verdana'})


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
    Output('scorecard2', 'figure'),
    Output('confirm', 'displayed')

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
def update_graph(crypto1, crypto2,n ,lin_log, data_type, picked_date, invest_value, invest_date):

    invest_date = datetime.strptime(invest_date, '%Y-%m-%d')

    picked_start_date = pd.to_datetime(str(picked_date[0])+"-01-01")  #date(2014,1,1)#date(picked_date[0],1,1)
    if str(picked_date[1]) == '2021':
        picked_end_date = pd.to_datetime(str(picked_date[1]) + "-05-26")
    else:
        picked_end_date = pd.to_datetime(str(picked_date[1])+"-12-01") #date(picked_date[1],12,31)

    ######################################## AUX COLUMNS FOR PROFIT #############################################

    ## checks if the invest date happens after the data available for the currency
    crypto1_firstdate = list(prices[(prices["Currency"] == crypto1)]["Date"])[0]

    if crypto1_firstdate > invest_date:
        cryptoprice_1 = list(prices[(prices["Date"] == crypto1_firstdate) & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]
    else:
        cryptoprice_1 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]

    cryptonumber_1 = invest_value / cryptoprice_1

    ## checks if the invest date happens after the data available for the currency
    crypto2_firstdate = list(prices[(prices["Currency"] == crypto2)]["Date"])[0]

    if crypto2_firstdate > invest_date:
        cryptoprice_2 = list(prices[(prices["Date"] == crypto2_firstdate) & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]
    else:
        cryptoprice_2 = list(prices[(prices["Date"] == invest_date) & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]

    cryptonumber_2 = invest_value / cryptoprice_2



    #calculates profit
    prices["Profit 1"] = prices[prices["Currency"] == crypto1]["Closing Price (USD)"].apply(lambda line: line * cryptonumber_1)
    prices["Profit 2"] = prices[prices["Currency"] == crypto2]["Closing Price (USD)"].apply(lambda line: line * cryptonumber_2)

    prices["Profit 1"] = prices["Profit 1"].fillna(0)
    prices["Profit 2"] = prices["Profit 2"].fillna(0)

    prices["Profit ($)"] = prices["Profit 1"] + prices["Profit 2"]

    ######################################## LINE CHART #############################################

    line_data = []
    if invest_date < picked_start_date:
        prices_dates = prices[(prices["Date"] >= invest_date) & (prices["Date"] <= picked_end_date)]
    else:
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

    if lin_log == "linear":
        fig_line_chart.add_annotation(bgcolor="#F5F3F6", opacity=0.95, y=max_crypto1, x=max_date_crypto1, text=("Max "+ data_type + " for " + crypto1 + " : " + str(round(max_crypto1,2))) ,showarrow=True,arrowhead=1)
        fig_line_chart.add_annotation(bgcolor="#F5F3F6", opacity=0.95, y=max_crypto2, x=max_date_crypto2, text=("Max "+ data_type + " for " + crypto2+ " : " + str(round(max_crypto2,2))), showarrow=True,arrowhead=1)
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
    cryptonumber1 = invest_value / cryptoprice_1

    crypto_lastprice1 = list(prices[(prices["Date"] == '26/05/2021') & (prices["Currency"] == crypto1)]["Closing Price (USD)"])[0]

    profit1 = (cryptonumber1 * crypto_lastprice1)

    scorecard1 = go.Figure(go.Indicator(
        mode="number+delta",
        value=round(float(profit1), 2),
        number={'prefix': "$"},
        delta={'position': "bottom", 'reference': invest_value, 'relative' :True},
    ))
    scorecard1.update_layout(title = {
        'text': crypto1,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}, width=200, height=100, margin=dict(l=10, r=10, b=10, t=30), plot_bgcolor='rgba(0,0,0,0)')

    #################### SCORECARD 2 CHART #########################
    cryptonumber2 = invest_value / cryptoprice_2

    crypto_lastprice2 = list(prices[(prices["Date"] == '26/05/2021') & (prices["Currency"] == crypto2)]["Closing Price (USD)"])[0]

    profit2 = (cryptonumber2 * crypto_lastprice2)

    scorecard2 = go.Figure(go.Indicator(
        mode="number+delta",
        value=round(float(profit2), 2),
        number={'prefix': "$"},
        delta={'position': "bottom", 'reference': invest_value, 'relative' :True},
    ))
    scorecard2.update_layout(title = {
        'text': crypto2,
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},width=200, height=100, margin=dict(l=10, r=10, b=10, t=30), plot_bgcolor='rgba(0,0,0,0)')

    if (invest_date < crypto1_firstdate) or (invest_date < crypto2_firstdate):
        confirm_answer = True
    else:
        confirm_answer =  False

    return fig_line_chart, \
           fig_radar_chart, \
           table1, \
           table2, \
           image1, \
           image2, \
           scorecard1, \
           scorecard2, \
           confirm_answer


if __name__ == '__main__':
    app.run_server(debug=True)
