import requests
from bs4 import BeautifulSoup as BS 

url='https://news.ycombinator.com'

r=requests.get(url)

html=r.text

soup=BS(html,'html.parser')

for first in soup.find_all("table",id="hnmain"):
	for second in first.find_all("table",class_="itemlist"):
		for third in second.find_all("tr",class_="athing"):
			for fourth in third.find_all("td",class_="title"):
				for fifth in fourth.find_all("a",class_="storylink"):
					print fifth.text