import requests
from bs4 import BeautifulSoup

class StockData:
    def getStockPrice(self, ticker):
        data = requests.get('https://finance.yahoo.com/quote/' + str(ticker))
        soup = BeautifulSoup(data.text, 'html.parser')
        return str(soup.find_all('span')[14]).split('>')[1].split('<')[0]

    # Add more methods here
