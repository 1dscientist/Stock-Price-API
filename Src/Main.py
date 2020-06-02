# Stock Data API
import Data
from flask import Flask

app = Flask(__name__)
stockData = Data.StockData()

@app.route('/')
def hello_world():
    return 'Welcome to the Stock Data API'

@app.route('/stocks')
def stocks():
    return 'Use Endpoints to Look Up Stock Data'
@app.route('/stocks/<ticker>')
def stockPrice(ticker):
    return str(stockData.getStockPrice(ticker))

if __name__ == '__main__':
    app.run()