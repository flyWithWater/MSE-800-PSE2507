1. import requests

2. from bs4 import BeautifulSoup
3.
4. url = 'http://example.com/quotes'
5. response = requests.get(url)
6. soup = BeautifulSoup(response.text, 'html.parser')
7.
8. quotes = soup.find_all('div', class_='quote')
9.
10. for quote in quotes:
11. print(quote.text)