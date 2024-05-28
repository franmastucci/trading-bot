# data_fetcher.py

import yfinance as yf

def get_historical_data(symbol, start_date, end_date):
    btcusdt_data = yf.download(symbol, start=start_date, end=end_date, interval='1m')
    return btcusdt_data
