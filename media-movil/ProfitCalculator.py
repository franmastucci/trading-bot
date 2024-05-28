class ProfitCalculator:
    @staticmethod
    def calculate_profit_percentage(data):
        buy_prices = data[data['Signal'] == 'BUY']['Close'].values
        sell_prices = data[(data['Signal'] == 'SELL') | (data['Signal'] == 'STOP_LOSS_LONG')]['Close'].values
        sell_short_prices = data[data['Signal'] == 'SELL_SHORT']['Close'].values
        cover_short_prices = data[(data['Signal'] == 'COVER_SHORT') | (data['Signal'] == 'STOP_LOSS_SHORT')]['Close'].values

        if len(buy_prices) == 0 and len(sell_short_prices) == 0:
            return 0.0

        total_profit_percentage = 0.0

        # Calculate profit for long trades
        trades_count = min(len(buy_prices), len(sell_prices))
        for i in range(trades_count):
            buy_price = buy_prices[i]
            sell_price = sell_prices[i]
            total_profit_percentage += ((sell_price - buy_price) / buy_price) * 100

        # Calculate profit for short trades
        trades_count = min(len(sell_short_prices), len(cover_short_prices))
        for i in range(trades_count):
            sell_short_price = sell_short_prices[i]
            cover_short_price = cover_short_prices[i]
            total_profit_percentage += ((sell_short_price - cover_short_price) / sell_short_price) * 100

        return total_profit_percentage
