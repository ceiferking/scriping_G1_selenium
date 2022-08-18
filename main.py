# import webdriver
from fileinput import close
from hashlib import scrypt
from multiprocessing.resource_sharer import stop
from turtle import pd
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import time
import pandas as pd

# create webdriver object
#navegador = webdriver.Chrome()

opitions = Options()
#oculta navegador
#opitions.add_argument('==headdless') 
#define tamanho do navegador
#opitions.add_argument('window-size=1100,800')
#carrega o web drive do navegador
navegador = webdriver.Chrome(options=opitions)
#acessa o site disponibilisado pelo usuario

#recebe link da kabum onde queira extrair dados
url = 'https://g1.globo.com/tecnologia'

navegador.maximize_window()

navegador.get(url)

sleep(3)

for contador in range(15):
    sleep(1)
    navegador.execute_script("window.scrollBy(0, 400)")
    sleep(1)
    navegador.execute_script("window.scrollBy(0, 400)")


sleep(4)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

noticia = site.findAll('div', attrs={'class': 'feed-post-body'})

#cria uma lista para receber dados
dic_noti = []

#percorre todas noticias carreagadas
for noticia in noticia:
    titulo = noticia.find('a', attrs={'class':'feed-post-link'})
    subtitulo = noticia.find('div', attrs={'class':'feed-post-body-resumo'})
     
     #Adiciona os dados estraidos para uam lista ordenada
    if (subtitulo):
         dic_noti.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        dic_noti.append([titulo.text, '',titulo['href']])
#cria tabela de dados para receber as informações
df = pd.DataFrame(dic_noti, columns=['Título', 'Subtítulo', 'Link'])

df.to_csv('noticia_pd.csv', encoding='utf-8', sep=';')