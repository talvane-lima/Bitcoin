import plotly
import pandas as pd
import requests
import sys
import plotly.plotly as py
from plotly.graph_objs import *
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

#List of the coins
coins = ['bitcoin', 'iota', 'ethereum', 'monero','litecoin', 'ripple', 'dash', 'zcoin', 'lisk','neo','eos','waves','golem','stratis','vertcoin','siacoin','verge']

csv = []
for c in coins:
	csv.append(pd.read_csv(StringIO(requests.get("https://www.coingecko.com/price_charts/export/"+c+"/brl.csv").content.decode('utf-8')), sep=","))

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash('offline example')

trace = []
for df in csv:
	trace.append(Scatter(x=df['snapped_at'],y=df['price']))

dccs = []
for t in range(len(trace)):
	dccs.append(dcc.Graph(id=coins[t], figure={'data': [trace[t]], 'layout': {'title': coins[t].lower().capitalize()}}))

app.layout = html.Div(dccs)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True)