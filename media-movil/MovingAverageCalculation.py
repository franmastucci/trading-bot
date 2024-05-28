class MovingAveragesCalculator:
    @staticmethod
    def calculate_moving_averages(prices, short_window=7, long_window=55, trend_window=50):
        short_ma = prices.rolling(window=short_window).mean()
        long_ma = prices.rolling(window=long_window).mean()
        trend_ma = prices.rolling(window=trend_window).mean()
        return short_ma, long_ma, trend_ma
