#WEB SCRAPING sacando informacion de paginas web

#librerias que se deben instalar

# pip install requests

# pip install lxml

# pip install beautifulsoup4

import requests

from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}


url = 'https://stackoverflow.com/questions'


respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text, 'lxml')
contenedor_de_preguntas = soup.find(id='questions')
lista_preguntas = contenedor_de_preguntas.find_all('div', class_ = 's-post-summary')

for pregunta in lista_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_ = 's-post-summary--content-excerpt').text
    print(texto_pregunta)
    print(descripcion_pregunta)

