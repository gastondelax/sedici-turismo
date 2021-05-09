# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:06:38 2021

@author: gaston
"""

###########################################
#################LIBRERIAS#################
import requests
from bs4 import BeautifulSoup
import pandas as pd
###########################################
#####LISTA DE LINKS DE TESIS TURISMO#######
#obtengo web a scrapear
url= 'http://sedici.unlp.edu.ar/handle/10915/34/discover?rpp=200&etal=0&group_by=none&page=1&sort_by=dc.date.accessioned_dt&order=desc&filtertype_0=type&filter_relational_operator_0=equals&filter_0=Tesis+de+grado'
p = requests.get(url)
soup = BeautifulSoup(p.text, 'html.parser')
###uso dos lists para obtener los links de cada ficha (tesis)
enlaces = list()
listado = list()
for i in soup.find_all('span', {'class':'title'}):
    per_review = i.find('a')
    enlaces.append(per_review)
for tag in enlaces:
    listado.append(tag.get('href'))
                ###dataframe final
df = pd.DataFrame(listado, columns = ['hoja'])
df.insert(0, 'tallo', 'http://sedici.unlp.edu.ar')
df["Links"] = df["tallo"] + df["hoja"]
df.drop(columns =['hoja', 'tallo'], inplace = True)
df.to_csv('links.csv')
###########################################
#######REVISION DE LISTADO#################
#Para este caso, no hay tesis de turismo anterior a 1997. 
titulo = list()
fecha_expo = list()
aux2=list()
links = pd.read_csv('links.csv', header=0)
lista_links = links['Links'].to_list()
for i in lista_links:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    for t in soup.find_all('h1'):
        titulo.append(t.text)
    for d in soup.find(class_ = 'metadata simple-item-view-other date-exposure'):
        aux2.append(d.string)
    fecha_expo.append(str(aux2[3]))
    aux2=list()
tabla = pd.DataFrame(list(zip(titulo, fecha_expo)),
                         columns = ['Titulo', 'Fecha de exposición', 
                                    ])
#puedo hacer la revisión en tabla excel
tabla.to_excel('revision.xlsx', encoding='utf-8')
#Si los links son correctos, entonces se pasa 
#al paso 2: extracción de los campos de cada ficha
###########################################

