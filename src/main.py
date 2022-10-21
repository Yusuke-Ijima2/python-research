import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI, Response


load_url = 'https://zuma-lab.com/'
data = requests.get(load_url)
html = BeautifulSoup(data.content, 'html.parser')

html_element = html.find_all('h4') #スクレイピングしたデータの配列
html_list = [] #スクレイピングしたデータをこの変数に格納

for i in range(10):
  html_list.append(html_element[i].text)

# print(html_list)

app = FastAPI()

@app.get("/scraping-data")
def read_root(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return { "data" : html_list }

