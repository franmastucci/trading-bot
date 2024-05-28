def calculate_profit_percentage(data):
    buy_signals = data[data['Signal'] == 'BUY']
    sell_signals = data[data['Signal'] == 'SELL']

    profit_percentage = 0.0

    if len(buy_signals) > 0 and len(sell_signals) > 0:
        buy_price = buy_signals.iloc[0]['Close']
        sell_price = sell_signals.iloc[0]['Close']

        profit_percentage = ((sell_price - buy_price) / buy_price) * 100

    return profit_percentage
