# importa bibliotecas
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import csv


# Recebe o link da pagina de noticias
URL = "https://g1.globo.com/tecnologia/index/feed/pagina-1.ghtml"

# indica o headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

# Faz o get da pagina
r = requests.get(URL, headers=headers)

# Transforma o get do webdriver em um objeto no BeutifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# cria uma lista para receber dados
dic_noti = []

# Percorre todas paginas do site estipuladas no "range"

for i in range(1, 2000):

    url_pag = f'https://g1.globo.com/tecnologia/index/feed/pagina-{i}.ghtml'
    r = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    noticia = soup.find_all('div', attrs={'class': 'feed-post-body'})

    # Percorre todas noticias da pagina estipulada
    for noticia in noticia:

        titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
        subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
        
         # Adiciona os dados estraidos para uam lista ordenada
        if (subtitulo):
            dic_noti.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            dic_noti.append([titulo.text, '', titulo['href']])
    print(url_pag)
    # cria tabela de dados para receber as informações
df = pd.DataFrame(dic_noti, columns=['Título', 'Subtítulo', 'Link'])

df.to_excel('rapagem_g1.xls')
