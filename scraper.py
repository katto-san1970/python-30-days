import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

knigi = soup.find_all("article", class_="product_pod")

print(f"Всего книг: {len(knigi)}")
print("-" * 30)

for kniga in knigi:
    nazvan = kniga.find("h3").find("a")["title"]
    cena = kniga.find("p", class_="price_color").text
    print(f"Название: {nazvan}")
    print(f"Цена: {cena}")
    print()

    