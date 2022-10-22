import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, Response

txt_file = open("test.txt")
reader = txt_file.read()
txt_file.close()
reader = reader.split("\n")
# print(reader)

# load_url = 'https://zuma-lab.com/'
load_url = reader[2] #間違えて2行入れてしまった時用
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

