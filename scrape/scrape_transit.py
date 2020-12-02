from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import time
import pandas as pd
import pymongo
import datetime as dt

# conn='mongodb://localhost:27017'
# client = pymongo.MongoClient(conn)
# db=client.transitDB

def scrape_all():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    google_url = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRGRpYzNrU0FtVnVLQUFQAQ/sections/CAQqEAgAKgcICjCj9vAKMM_ruwIwqaLKBQ?hl=en-US&gl=US&ceid=US%3Aen'
    browser.visit(google_url)

    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    try:
        google_title = soup.find('h3',class_='ipQwMb ekueJc RD0gLb').text.strip()
    except: 
        google_title = '[No information returned. Click the button again.]'
    try:
        google_para = soup.find('div',class_='Da10Tb Rai5ob').text.strip()
    except:
        google_para = '[No information returned.  Click the button again.]'
    try:
        google_source = soup.find('a',class_='wEwyrc AVN2gc uQIVzc Sksgp').text.strip()
    except:
        google_source = '[No information returned.  Click the button again.]'
    try:
        google_date = soup.find('time',class_='WW6dff uQIVzc Sksgp').text.strip()
    except:
        google_date = '[No information returned.  Click the button again.]'

    browser.quit()

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    transitmag_url = 'https://www.masstransitmag.com/'
    browser.visit(transitmag_url)
    transitmag_source = 'Mass Transit Magazine'

    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    try:
        transitmag_title = soup.find('h5',class_='node__title').text.strip()
    except: 
        transitmag_title = '[No information returned. Click the button again.]'
    try:
        transitmag_para = soup.find('div',class_='node__text node__text--teaser').text.strip()
    except:
        transitmag_para = '[No information returned.  Click the button again.]'
    try:
        transitmag_date = soup.find('div',class_='node__footer-right').text.strip()
    except:
        transitmag_date = '[No information returned.  Click the button again.]'

    browser.quit()

    data = {
        'google_news_title':google_title,
        'google_news_paragraph':google_para,
        'google_news_source':google_source,
        'google_news_date':google_date,
        'google_url':google_url,
        'transitmag_title':transitmag_title,
        'transitmag_paragraph':transitmag_para,
        'transitmag_source':transitmag_source,
        'transitmag_date':transitmag_date,
        'transitmag_url':transitmag_url
    }

    return(data)

