class TrendDetector:
    @staticmethod
    def determine_trend(trend_ma):
        trend = []
        for i in range(1, len(trend_ma)):
            if trend_ma.iloc[i] > trend_ma.iloc[i-1]:
                trend.append('Bullish')
            elif trend_ma.iloc[i] < trend_ma.iloc[i-1]:
                trend.append('Bearish')
            else:
                trend.append('Sideways')
        trend.insert(0, 'Sideways')  # First value to match the length of trend_ma
        return trend
