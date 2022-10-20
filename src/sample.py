import requests
from bs4 import BeautifulSoup

load_url = 'https://zuma-lab.com/'
data = requests.get(load_url)
html = BeautifulSoup(data.content, 'html.parser')

html_list = []

for element in html.find_all('h4'):
  html_list.append(element.text)

print(html_list)
