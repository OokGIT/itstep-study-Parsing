import requests
import bs4
URL = 'https://feerie.com.ua/ua/all-tours/'
# HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
#            'accept': '*/*'}
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'}
HOST = 'https://feerie.com.ua'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='col-xs-6')
#    print(items)
    tours = []
    for item in items:
        tours.append({
            'title': item.find('div', class_='field field--name-node-title field--type-ds field--label-hidden field--item').get_text(strip=True),
            'link': HOST + item.find('a', href=True).attrs['href'],
            'price': item.find('div', class_='field field--name-ftf-discount-price-actual field--type-string field--label-hidden field--item').get_text(),
            'country': item.find('span', class_='field-content').get_text()
        })
    print(tours)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error on page, not 200 response')


parse()
