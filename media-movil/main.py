from TradingBot import  TradingBot


if __name__ == "__main__":

    # Símbolos de índices financieros
    SP500 = "^GSPC"
    DOW_JONES = "^DJI"
    NASDAQ = "^IXIC"
    RUSSELL2000 = "^RUT"
    FTSE100 = "^FTSE"
    NIKKEI225 = "^N225"
    DAX = "^GDAXI"
    CAC40 = "^FCHI"
    HANG_SENG = "^HSI"

    # Símbolos de acciones populares
    APPLE = "AAPL"
    MICROSOFT = "MSFT"
    AMAZON = "AMZN"
    TESLA = "TSLA"
    ALPHABET_A = "GOOGL"  # Clase A
    ALPHABET_C = "GOOG"   # Clase C

    # Símbolos de bonos y fondos
    US_10Y_TREASURY = "^TNX"
    US_2Y_TREASURY = "^IRX"
    SPDR_SP500_ETF = "SPY"
    INVESCO_QQQ = "QQQ"
    VANGUARD_EMERGING_MARKETS = "VWO"

    # Símbolos de materias primas y otros derivados
    GOLD_FUTURES = "GC=F"
    CRUDE_OIL = "CL=F"
    SILVER_FUTURES = "SI=F"
    EURO_FUTURES = "6E=F"

    # Pares de criptomonedas
    BTC_USD = "BTC-USD"  # Bitcoin to US Dollar
    ETH_USD = "ETH-USD"  # Ethereum to US Dollar
    XRP_USD = "XRP-USD"  # Ripple to US Dollar
    LTC_USD = "LTC-USD"  # Litecoin to US Dollar
    ADA_USD = "ADA-USD"  # Cardano to US Dollar
    DOT_USD = "DOT-USD"  # Polkadot to US Dollar

# Definir los parámetros para el bot de trading
    symbol = BTC_USD
    start_date = '2024-04-21'
    end_date = '2024-05-25'
    short_window = 7
    long_window = 55
    trend_window = 50
    stop_loss_percent = 1

    # Crear una instancia del bot de trading
    bot = TradingBot(symbol, start_date, end_date, short_window, long_window, trend_window, stop_loss_percent)

    # Ejecutar el bot de trading
    bot.run()

#
#    symbol = "EURUSD=X"
#    start_date = '2024-05-21'
#    end_date = '2024-05-22'
#    short_window = 7
#    long_window = 55
#    trend_window = 50
#    stop_loss_percent = 1


# Símbolos de `yfinance` para diferentes activos e índices financieros
