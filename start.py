import requests
import bs4
import csv
import re

URL = 'https://feerie.com.ua/ua/all-tours/'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
           'accept': '*/*'}
HOST = 'https://feerie.com.ua'
EXPORT_CSV = 'feerie_parse.csv'

# Находим номер последней странички в пагинации
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
pages_count = int(re.findall('(?<=page\=)\d+', str(soup.find("li", class_="pager__item pager__item--last")))[0])


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def save_csv(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название тура', 'ссылка', 'Цена', 'Страна'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['country']])


def get_content(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-xs-6')
#    print(items)
    tours = []
    for item in items:
        price_field = item.find('div', class_='field field--name-ftf-discount-price-actual field--type-string field--label-hidden field--item').get_text().replace('від ', '')
        tours.append({
            'title': item.find('div', class_='field field--name-node-title field--type-ds field--label-hidden field--item').get_text(strip=True),
            'link': HOST + item.find('a', href=True).attrs['href'],
            # 'price': item.find('div', class_='field field--name-ftf-discount-price-actual field--type-string field--label-hidden field--item').get_text(),
            'price': price_field,
            'country': item.find('span', class_='field-content').get_text()
        })
    return(tours)


def parse():
    # pages_count = input('Сколько страниц парсить?')
    # pages_count = int(pages_count.strip())
    html = get_html(URL)
    if html.status_code == 200:
        tours = []
        for page in range(0, pages_count):
            print('Парсинг страницы', page + 1)
            html = get_html(URL, params={'page': page})
            tours.extend(get_content(html.text))
            save_csv(tours, EXPORT_CSV)
        # get_content(html.text)
        print('Готово, результаты записаны в файл', EXPORT_CSV)
        # print(tours)
    else:
        print('Error on page, not 200 response')

parse()
