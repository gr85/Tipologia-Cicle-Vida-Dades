# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime 

r = requests.get('https://resultados.as.com/resultados/baloncesto/nba/clasificacion/')

soup = BeautifulSoup(r.content, "html.parser")

data = []
table = soup.findAll('table', attrs={'class': 'tabla-datos'})
date = datetime.datetime.now().strftime('%Y/%m/%d')
time = datetime.datetime.now().strftime('%H:%M:%S')
date_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

for t in table:
    rows = t.find_all('tr')
    division = ''
    new_div = ''
    for i,row in enumerate(rows):
        new_div = row.find('td', class_='s-left')
        if new_div != '' and new_div != division and new_div != None:
            division = new_div.string
        if i not in range(3,8) and i not in range(9,14) and i not in range(15,20):
            continue
        pos = row.find('span', attrs={'class': 'pos'})
        name = row.find('span', attrs={'class': 'nombre-equipo'})
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([date, time, division, pos.string, name.string, 
                     cols[0], cols[1], cols[2], cols[3], cols[4], cols[5]])
    

df = pd.DataFrame(data, columns=['Date', 'Time', 'Division', 'Position', 'Team', 'GamesPlayed', 
                                 'Won', 'Lost', 'PointsAgainst', 'PointsForth', 'DiffPoints'])

filename = date_time + '_NBA.csv'
df.to_csv(path_or_buf='D:\\_UOC\\Master Data Science\\3_Tipologia cicle vida dades\\PACS\\PRA1\\'+filename,
          sep=';', index=False)

#df.head()

print(datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))