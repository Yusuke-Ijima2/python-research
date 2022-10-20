import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI


load_url = 'https://zuma-lab.com/'
data = requests.get(load_url)
html = BeautifulSoup(data.content, 'html.parser')

html_list = [] #スクレイピングしたデータをこの変数に格納

for element in html.find_all('h4'):
  html_list.append(element.text)

print(html_list)

app = FastAPI()

@app.get("/scraping-data")
def read_root():
    return { "data" : html_list }

