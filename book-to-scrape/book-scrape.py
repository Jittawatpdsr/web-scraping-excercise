import requests
import pandas as pd
from bs4 import BeautifulSoup

books_data = []

for i in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    get_data = requests.get(url)

    data = BeautifulSoup(get_data.text,'html.parser')

    find_ol = data.find('ol')
    articles = find_ol.find_all('article',{'class':'product_pod'})

def scrape_books(articles):
    global books_data
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']

        star = article.find('p')
        star = star['class'][1]

        price = article.find('p',{'class':'price_color'}).text
        price = str(price[1:])
        price = price.replace('£','')

        books_data.append([title, price, star])

scrape_books(articles)

df = pd.DataFrame(books_data,columns=['Title','Price','Star Rating'])

df.to_csv('book-to-scrape.csv')