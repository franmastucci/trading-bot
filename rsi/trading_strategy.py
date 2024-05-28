import pandas as pd

def calculate_rsi(prices, window=14):
    delta = prices.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_signals(prices, rsi, buy_threshold=30, sell_threshold=70):
    signals = []
    min_length = min(len(prices), len(rsi))
    is_trade_open = False  # Indica si hay una operación abierta

    for i in range(min_length):
        if rsi.iloc[i] < buy_threshold:  # RSI por debajo del umbral de sobreventa
            if not is_trade_open:  # Si no hay una operación abierta, abrir una nueva
                signals.append('BUY')
                is_trade_open = True
            else:
                signals.append('HOLD')
        elif rsi.iloc[i] > sell_threshold:  # RSI por encima del umbral de sobrecompra
            if is_trade_open:  # Si hay una operación abierta, cerrarla
                signals.append('SELL')
                is_trade_open = False
            else:
                signals.append('HOLD')
        else:
            signals.append('HOLD')

    return signals
