class SignalGenerator:
    @staticmethod
    def generate_signals(prices, short_ma, long_ma, stop_loss_percent, trend):
        signals = []
        min_length = min(len(prices), len(short_ma), len(long_ma), len(trend))

        long_trade_open = False  # Indicates if there is an open long trade
        short_trade_open = False  # Indicates if there is an open short trade
        buy_price = 0
        sell_short_price = 0

        for i in range(min_length):
            if trend[i] == 'Bullish':
                if short_ma.iloc[i] > long_ma.iloc[i]:  # Bullish crossover of moving averages
                    if not long_trade_open and not short_trade_open:  # Open a new long trade if no trade is open
                        signals.append('BUY')
                        long_trade_open = True
                        buy_price = prices.iloc[i]
                    else:
                        signals.append('HOLD')
                elif long_trade_open and prices.iloc[i] < buy_price * (1 - stop_loss_percent / 100):  # Check for stop loss in long trade
                    signals.append('STOP_LOSS_LONG')
                    long_trade_open = False
                elif long_trade_open and short_ma.iloc[i] < long_ma.iloc[i]:  # Bearish crossover of moving averages
                    signals.append('SELL')
                    long_trade_open = False
                else:
                    signals.append('HOLD')
            elif trend[i] == 'Bearish':
                if short_ma.iloc[i] < long_ma.iloc[i]:  # Bearish crossover of moving averages
                    if not short_trade_open and not long_trade_open:  # Open a new short trade if no trade is open
                        signals.append('SELL_SHORT')
                        short_trade_open = True
                        sell_short_price = prices.iloc[i]
                    else:
                        signals.append('HOLD')
                elif short_trade_open and prices.iloc[i] > sell_short_price * (1 + stop_loss_percent / 100):  # Check for stop loss in short trade
                    signals.append('STOP_LOSS_SHORT')
                    short_trade_open = False
                elif short_trade_open and short_ma.iloc[i] > long_ma.iloc[i]:  # Bullish crossover of moving averages
                    signals.append('COVER_SHORT')
                    short_trade_open = False
                else:
                    signals.append('HOLD')
            else:
                signals.append('HOLD')

        # Ensure the length of signals matches the length of the prices
        if len(signals) < len(prices):
            signals.extend(['HOLD'] * (len(prices) - len(signals)))

        return signals
