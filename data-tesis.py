# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:59:33 2021

@author: gaston
"""

###########################################
#################LIBRERIAS#################
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#####################################################
#################DATA TESIS##########################
######LISTAS#####
#personas
autor = list()
aux0 = list()
aux1 = list()
director = list()
#tesis
titulo = list()
subtitulo = list()
fecha_expo = list()
aux2=list()
resumen = list()
#Tesis-palabras clave OK
key0=list()
key1=list()
key2=list()
key3=list()
key4=list()
key5=list()
#####Links en list para iterar#####
links = pd.read_csv('links.csv', header=0)
lista_links = links['Links'].to_list()
#####ITERACION SOBRE CADA LINK#####
for i in lista_links:
    r = requests.get(i)
    soup = BeautifulSoup(r.text, 'html.parser')
    ###Data de Tesis
    for t in soup.find_all('h1'):
        titulo.append(t.text)
    for s in soup.find_all('span', class_= 'metadata-value', limit=1):
        subtitulo.append(s.text)
    for d in soup.find(class_ = 'metadata simple-item-view-other date-exposure'):
        aux2.append(d.string)
    fecha_expo.append(str(aux2[3]))
    aux2=list()
    for r1 in soup.find_all('div', class_='simple-item-view-description', limit=1):
        texto = r1.text
    resumen.append(texto[10:])
   ###Data Palabras claves
    for i in soup.find_all(href=re.compile('keywords'), limit=5):
        col1=i.string
        key0.append(col1.string)
    key1.append(key0[0]) #columna 1 siempre va a entrar
    if len(key0) > 1:   #las siguientes columnas condicional
        key2.append(key0[1])
    else:
        key2.append('s/d')
    if len(key0) > 2:
        key3.append(key0[2])
    else:
        key3.append('s/d')
    if len(key0) > 3:
        key4.append(key0[3])
    else:
        key4.append('s/d')
    if len(key0) > 4:
        key5.append(key0[4])
    else:
        key5.append('s/d')
    key0=list()   
    ###Data de Personas (Autor, Director)
    aux0 = soup.find_all('a', href=re.compile('author'))
    for t in aux0:
        aux1.append(t.text)
    autor.append(aux1[1])
    if len(aux1) > 2:
        director.append(aux1[2])
    else:
        director.append('s/d')
    aux1=list()
#########ARMADO DE TABLA PRINCIPAL###############
tabla = pd.DataFrame(list(zip(titulo, subtitulo, autor, director, fecha_expo, key1, key2, key3, key4, key5, resumen)),
                         columns = ['Titulo','Subtitulo', 'Autor', 'Director', 'Fecha de exposición', 
                                    'Palabra clave 1', 'Palabra clave 2', 'Palabra clave 3', 'Palabra clave 4', 'Palabra clave 5', 'Resumen'
                                    ])

####EXPORTO TABLA A CSV Y EXCEL########
tabla.to_csv("turismo-sedici.csv", encoding='utf-8')
tabla.to_excel('turismo-sedici.xlsx', encoding='utf-8')

#######################################################

