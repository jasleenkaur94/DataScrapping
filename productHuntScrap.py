import requests
from bs4 import BeautifulSoup as BS

url='https://producthunt.com'

r=requests.get(url)

html=r.text

soup=BS(html,'html.parser')

for first in soup.find_all("main",id="app"):
	for second in first.find_all("div"):
		for third in second.find_all("div"):
			for a in first.find_all("div",class_="content_1mxGg"):	
				for div in a.find_all("div",class_="legacyPosts_3AHFn"):
					for ul in div.find_all("ul",class_="postsList_3n2Ck"):
						for li in ul.find_all("li"):
							for s in li.find_all("div",class_="postItem_RepXj"):
								for p in s.find_all("div",class_="content_3Qj0y"):
									for q in p.find_all("span",class_="title_24w6f featured_2PenR default_25TkV base_3LqBu"):
										print q.text
"""b=a.find_all(")[0]
l= b.find_all("ul",class_="postsList_3n2Ck")[0]

ul=ls.find_all("li")[0]
li=ul.find_all("div",class_="postItem_RepXj")[0]
s=li.find_all("div",class_="content_3Qj0y")[0]
p=s.find_all("span",class_="title_24w6f featured_2PenR default_25TkV base_3LqBu")

print """
