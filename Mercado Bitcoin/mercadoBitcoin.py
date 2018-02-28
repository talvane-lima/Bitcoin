import requests
import re
from bs4 import BeautifulSoup
import json
import time
from bashplotlib.scatterplot import plot_scatter

search = 'BTC'
method = 'ticker'

buy_value = 50650 #Set the buy value
interval = 5 #Minutes

xy_file = "xy.txt"
count = 0
file = open(xy_file, 'w')
file.close()
while(True):
	file = open(xy_file, 'a')
	try:
		page = requests.get("https://www.mercadobitcoin.net/api/"+search+"/"+method+"/")
	except Exception as e:
		continue
	count += 1
	data_json = json.loads(str(BeautifulSoup(page.content, 'html.parser')))
	percent = (abs(float(data_json['ticker']['last'])-buy_value)/buy_value)*100
	file.write(str(count)+","+data_json['ticker']['last']+"\n")
	file.close()
	if float(data_json['ticker']['last']) >= buy_value:
		symb = u"\u2191"
	else:
		symb = u"\u2193"
	plot_scatter(xy_file, "", "", 30, "*", "red", data_json['ticker']['last']+" "+symb+" "+str(percent)+"%")
	time.sleep((interval-int(percent))*60)
	print chr(27) + "[2J"