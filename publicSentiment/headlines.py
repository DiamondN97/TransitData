#Import dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import time

####SCRAPING CODE#######
##Scraping Google News Aggregator for most recent transit news stories###
# URL of page to be scraped
transit_news = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRGRpYzNrU0FtVnVLQUFQAQ/sections/CAQqEAgAKgcICjCj9vAKMM_ruwIwqaLKBQ?hl=en-US&gl=US&ceid=US%3Aen'
# Retrieve page with the requests module
news_response = requests.get(transit_news)
# Create BeautifulSoup object; parse with 'lxml'
news_soup = bs(news_response.text, 'html')
#Find first headline to collect latest news title and paragraph text.
headlines = news_soup.find_all('article')
latest_news_title = headlines[0].text
latest_news_title = latest_news_title.strip()
print(latest_news_title)
