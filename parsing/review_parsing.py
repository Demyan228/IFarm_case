import requests
from bs4 import BeautifulSoup

# Задаём заголовки, похожие на те, что посылает реальный браузер
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/108.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,"
              "application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
}

url = "https://otzovik.com/?search_text=Эсциталопрам"

session = requests.Session()

# Присваиваем заголовки сессии
session.headers.update(headers)

response = session.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    product_links = []
    for a in soup.find_all('a', class_='product-name'):
        href = a.get('href')
        if href and href.startswith('/reviews/'):
            product_links.append("https://otzovik.com" + href)

    for link in product_links:
        print(link)
else:
    print(f"Ошибка {response.status_code} при загрузке страницы")