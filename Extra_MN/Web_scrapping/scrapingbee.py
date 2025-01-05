import requests as req
from bs4 import BeautifulSoup
import csv

# URL 
url = "https://www.scrapingbee.com/blog/web-scraping-101-with-python/"
response = req.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    main_title = soup.find('h1').text
    print(f"Título principal: {main_title}\n")

    headers = soup.find_all(['h2', 'h3'])
    links = soup.find_all('a', href=True)

    # Guardar en un archivo CSV
    with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tipo', 'Contenido'])

        writer.writerow(['Título principal', main_title])
        writer.writerow(['Encabezados'])
        for header in headers:
            writer.writerow(['Encabezado', header.text])


        writer.writerow(['Enlaces'])
        for link in links[:10]:  
            writer.writerow(['Enlace', link['href']])

    print("Datos guardados en scraped_data.csv")
else:
    print(f"Error al acceder a la página: {response.status_code}")