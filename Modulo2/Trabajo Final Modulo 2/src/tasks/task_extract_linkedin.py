import requests
from bs4 import BeautifulSoup
from prefect import task

url = 'https://www.linkedin.com/jobs/search/?currentJobId=4122356494&f_TPR=r86400&geoId=102927786&keywords=python'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

@task(name="Extracción de ofertas para LinkedIn")
def task_extract_linkedin():
    response = requests.get(url, headers=headers)
    ofertas = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ul_offers = soup.find('ul',{'class':'jobs-search__results-list'})
        lista_ofertas = ul_offers.find_all('li')

        for oferta in lista_ofertas:
            nombre_oferta = oferta.find('h3',{'class':'base-search-card__title'})
            ubicacion_oferta = oferta.find('span',{'class':'job-search-card__location'})
            url_oferta = oferta.find('a')
            empresa_oferta = oferta.find('a',{'class':'hidden-nested-link'})
            
            titulo = nombre_oferta.get_text().strip() if nombre_oferta else ''
            ubicacion = ubicacion_oferta.get_text().strip() if ubicacion_oferta else ''
            url_value = url_oferta['href'].strip() if url_oferta else ''
            compania = empresa_oferta.get_text().strip() if empresa_oferta else ''
            
            ofertas.append({"nombre": titulo, "ubicacion":ubicacion, "url": url_value,"empresa":compania})
        
    else:
        print(f'Error {response.status_code} {response.reason}')
    
    return ofertas
