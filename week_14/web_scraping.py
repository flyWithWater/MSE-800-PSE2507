import requests 
from bs4 import BeautifulSoup


"""
use BeautifulSoup to scrape the number of the coming event in a website.
"""

url = 'https://commeventshub.onrender.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='badge bg-primary')

for quote in quotes:
    print(quote.text)




