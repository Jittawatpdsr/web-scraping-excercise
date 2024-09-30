#30-9-2024_Jittawatp
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.naiin.com/category?bannerid=2512'
get_data = requests.get(url)

data = BeautifulSoup(get_data.text, 'html.parser')

title = data.find_all('a',{'class':'itemname'})
author = data.find_all('a',{'class':'inline-block tw-whitespace-normal tw-block'})
price = data.find_all('p',{'class':'txt-price'})


if len(title) == len(author) == len(price):

    books_data = []

    for title , author , price in zip(title,author,price):
        title_data = title.text.strip()
        author_data = author.text.strip()
        price_data = price.text.strip()

        print(f'title: {title_data}')
        print(f'author: {author_data}')
        print(f'price: {price_data} \n')

        books_data.append([title_data,author_data,price_data])

    df = pd.DataFrame(books_data,columns=['title','author','price'])
    df.to_csv('naiin-books.csv')