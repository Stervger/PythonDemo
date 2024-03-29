import requests
from bs4 import BeautifulSoup
import csv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
link = 'https://chongqing.anjuke.com/sale/'
r = requests.get(link,headers = headers)

soup = BeautifulSoup(r.text,'html.parser')
house_list = soup.find_all('li',class_ = 'list-item')
for house in house_list:
    name = house.find('div',class_ = 'house-title').a.text.strip()
    price = house.find('span', class_ = 'price-det').text.strip()
    price_area = house.find('span', class_ = 'unit-price').text.strip()
    nu_room = house.find('div', class_ ='details-item').span.text
    area = house.find('div', class_ ='details-item').contents[3].text
    floor = house.find('div', class_ ='details-item').contents[5].text
    year = house.find('div', class_ ='details-item').contents[7].text
    broker = house.find('span', class_='brokername').text
    broker = broker[1:]
    address = house.find('span', class_='comm-address').text.strip()
    tag_list = house.find_all('span', class_='item-tags')
    tag = [i.text for i in tag_list]
    print(name, price, price_area, nu_room, area, floor, year, broker, address, tag)




import requests
from bs4 import BeautifulSoup
import time
import csv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
for i in range(1,11):
    link = 'https://chongqing.anjuke.com/sale/p' + str(i)
    r = requests.get(link, headers=headers)
    print('现在爬取得是第',i , '页')

    soup = BeautifulSoup(r.text, 'html.parser')
    house_list = soup.find_all('li', class_='list-item')

    for house in house_list:
        name = house.find('div', class_='house-title').a.text.strip()
        price = house.find('span', class_='price-det').text.strip()
        price_area = house.find('span', class_='unit-price').text.strip()
        nu_room = house.find('div', class_='details-item').span.text
        area = house.find('div', class_='details-item').contents[3].text
        floor = house.find('div', class_='details-item').contents[5].text
        year = house.find('div', class_='details-item').contents[7].text
        broker = house.find('span', class_='brokername').text
        broker = broker[1:]
        address = house.find('span', class_='comm-address').text.strip()
        tag_list = house.find_all('span', class_='item-tags')
        tag = [i.text for i in tag_list]
        print(name, price, price_area, nu_room, area, floor, year, broker, address, tag)

    time.sleep(5)
