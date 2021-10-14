import requests
from bs4 import BeautifulSoup

URL = 'https://www.wildberries.ru/catalog/obuv/muzhskaya'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
HOST = 'https://www.wildberries.ru'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='dtList-inner')
    shoes = []
    for item in items:
        ss = item.find('ins', class_='lower-price')
        if ss:
            sff = ss.get_text()
        else:
            sff = 'none'
        shoes.append({
            'title': item.find('strong', class_='brand-name c-text-sm').get_text(strip=True).strip('/'),
            'link': HOST + item.find('a', class_='ref_goods_n_p j-open-full-product-card').get('href'),
            'price': sff

        })
    print(shoes)
    print(len(shoes))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
