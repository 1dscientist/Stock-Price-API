# Retrival of Stock data
import requests
from bs4 import BeautifulSoup

import StockPrice
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

class StockPrice:

    def getStockPrice(self, ticker):
        data = requests.get('https://finance.yahoo.com/quote/' + str(ticker))
        soup = BeautifulSoup(data.text, 'html.parser')
        return str(soup.find_all('span')[14]).split('>')[1].split('<')[0]

stocks = StockPrice()

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/<ticker>')
def stockPrice(ticker):
    return str(stocks.getStockPrice(ticker))

if __name__ == '__main__':
    app.run()