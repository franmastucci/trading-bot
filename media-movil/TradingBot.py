from SIgnalGenerator import SignalGenerator
from DataFetcher import DataFetcher
from MovingAverageCalculation import  MovingAveragesCalculator
from TrendDetector import TrendDetector
from ProfitCalculator import ProfitCalculator
from Plotter import Plotter



class TradingBot:
    def __init__(self, symbol, start_date, end_date, short_window=7, long_window=55, trend_window=50, stop_loss_percent=1):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.short_window = short_window
        self.long_window = long_window
        self.trend_window = trend_window
        self.stop_loss_percent = stop_loss_percent
        self.data = None
        self.short_ma = None
        self.long_ma = None
        self.trend_ma = None
        self.trend = None
        self.signals = None
        self.profit_percentage = None

    def fetch_data(self):
        self.data = DataFetcher.get_historical_data(self.symbol, self.start_date, self.end_date)

    def calculate_moving_averages(self):
        self.short_ma, self.long_ma, self.trend_ma = MovingAveragesCalculator.calculate_moving_averages(
            self.data['Close'], self.short_window, self.long_window, self.trend_window)

    def determine_trend(self):
        self.trend = TrendDetector.determine_trend(self.trend_ma)
        self.data['Trend'] = self.trend

    def generate_signals(self):
        self.signals = SignalGenerator.generate_signals(
            self.data['Close'], self.short_ma, self.long_ma, self.stop_loss_percent, self.trend)
        self.data['Signal'] = self.signals

    def calculate_profit(self):
        self.profit_percentage = ProfitCalculator.calculate_profit_percentage(self.data)
        print("Profit Percentage:", self.profit_percentage)

    def plot_results(self):
        Plotter.plot_signals(self.data, self.short_ma, self.long_ma, self.trend)

    def run(self):
        self.fetch_data()
        self.calculate_moving_averages()
        self.determine_trend()
        self.generate_signals()
        self.calculate_profit()
        self.plot_results()
