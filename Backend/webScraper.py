import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def urlExtract(url):
    response = requests.get(url)


    soup = bs(response.content, 'html.parser')

    img_div = soup.findAll("div",attrs={"class","_aagv"})
    for i in img_div:
        img_url = i.findAll("img", attrs="src")
