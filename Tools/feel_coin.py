# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from langdetect import *
search_coin = 'IOTA'
url = 'https://news.google.com/news/search/section/q/'+search_coin+'/'+search_coin+'?hl=en&gl=US&ned=us'

try:
	page = requests.get(url)
	page = BeautifulSoup(page.content, 'html.parser')
	news_link = page.find_all('a', class_="nuEeue hzdq5d ME7ew")
except:
	print('Error page')

for n_l in news_link:
	title = re.search(">(.+?)</a>", str(n_l)).group(1)
	try:
		print title, detect(title)
	except Exception as e:
		continue

from google.cloud import language

def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities


example_text = 'Python is such a great programming language'
sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)