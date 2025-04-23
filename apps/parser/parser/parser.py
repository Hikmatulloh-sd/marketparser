import requests
from bs4 import BeautifulSoup

base_url = 'https://lalafo.kg/'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36'
}


def parse_categories_name_url():
    res = requests.get(url=base_url, headers=headers)

    if res.status_code != 200:
        return f"Ошибка, код ответа {res.status_code}"

    soup = BeautifulSoup(res.text, 'lxml')
    category_items = soup.find_all('li', class_='main-menu-tab css-dr6rhu')
    categories = []

    for category in category_items:
        title_tag = category.find('p')
        link_tag = category.find('a')
        img_tag = category.find('img')

        title = title_tag.text.strip() if title_tag else 'Без названия'
        link = f"{base_url}{link_tag.get('href')}" if link_tag and link_tag.get('href') else 'Нет ссылки'
        img_link = img_tag.get('data-cfsrc') if img_tag and img_tag.get('data-cfsrc') else 'Нет изображения'

        categories.append({
            'title': title,
            'link': link,
            'img_link': img_link
        })

    return categories


# Для теста
for cat in parse_categories_name_url():
    print(cat)
