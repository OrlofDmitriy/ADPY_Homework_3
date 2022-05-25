import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Safari/537.36'
}
url = 'https://habr.com/ru/all/'

page = 1

while True:
    response = requests.get(url + 'page' + str(page), headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_snippets = soup.find_all(class_='tm-article-snippet')
    if len(all_snippets):
        for snippet in all_snippets:
            for keyword in KEYWORDS:
                if snippet.text.lower().find(keyword) > 0:
                    data = snippet.find('time').get('title')
                    header = snippet.find('h2').find('span').text
                    link = snippet.find('h2').find('a').get('href')
                    print(f'{data} - {header} - {"https://habr.com" + link}')
        page += 1
    else:
        break
