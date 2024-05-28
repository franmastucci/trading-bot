import data_fetcher
import trading_strategy
import signal_plotter
import profit_calculator

if __name__ == "__main__":
    # Example usage:
    start_date = '2024-05-10'
    end_date = '2024-05-15'
    btcusdt_df = data_fetcher.get_historical_data('BTC-USD', start_date, end_date)

    # Calculate RSI
    btcusdt_df['RSI'] = trading_strategy.calculate_rsi(btcusdt_df['Close'])

    # Generate signals
    btcusdt_df['Signal'] = trading_strategy.generate_signals(btcusdt_df['Close'], btcusdt_df['RSI'])

    # Extract buy and sell indices
    buy_indices = [i for i, signal in enumerate(btcusdt_df['Signal']) if signal == 'BUY']
    sell_indices = [i for i, signal in enumerate(btcusdt_df['Signal']) if signal == 'SELL']

    # Plot signals
    signal_plotter.plot_signals(btcusdt_df, buy_indices, sell_indices)

    # Calculate profit percentage
    profit_percentage = profit_calculator.calculate_profit_percentage(btcusdt_df)
    profit_percentage_formatted = "{:.2f}%".format(profit_percentage)
    print("Profit Percentage:", profit_percentage_formatted)
