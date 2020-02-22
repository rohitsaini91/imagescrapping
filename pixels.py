import bs4 as bs
import requests
import pandas as pd
import csv

req=requests.get('https://kaboompics.com/')
soup=bs.BeautifulSoup(req.content,'html.parser')
section=soup.find(class_="page-section pb-0 promoted")
div=section.find(class_="relative home-grid")
ul=div.find(class_="works-grid work-grid-gut clearfix font-alt hover-white hide-titles masonry")
listt=ul.find_all(class_="work-item mix all")
divv=[lis.find(class_="work-img") for lis in listt]
image=[img.find(class_="lazy blur-up")['data-src'] for img in divv]
df=pd.DataFrame({'image':image})
print(df)
