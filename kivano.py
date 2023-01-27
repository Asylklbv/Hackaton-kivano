import csv

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


URL = 'https://www.kivano.kg/mobilnye-telefony'


response = requests.get(URL)
html = response.text 


soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='item')

result = []
for tag in cards:
    title = tag.find('div', class_='listbox_title oh').text
    print(title)
    price = tag.find('div', class_='listbox_price').text
    img_link = tag.find('div', class_='listbox_img').find('img').get('src')
    
    obj = {
        'title': title.strip(),
        'price': price.strip(),
        'image_link': img_link,
    }
    result.append(obj)

with open('notebooks.csv', 'w') as file:
    names = ['title', 'price', 'image_link']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    for telefony in result:
        writer.writerow(telefony)

# print(result)