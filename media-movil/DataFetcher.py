import yfinance as yf


class DataFetcher:
    @staticmethod
    def get_historical_data(symbol, start_date, end_date):
        data = yf.download(symbol, start=start_date, end=end_date, interval='1h')
        return data
