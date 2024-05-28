import matplotlib.pyplot as plt

def plot_signals(data, buy_indices, sell_indices):
    plt.figure(figsize=(12, 10))

    # Price plot
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Close'], label='Precio', color='blue')
    plt.title('Precio del BTC-USD')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid(True)

    # Buy and sell signals
    for buy_index in buy_indices:
        plt.scatter(data.index[buy_index], data['Close'].iloc[buy_index], marker='^', color='green', label='Compra')
        next_sell_indices = [i for i in sell_indices if i > buy_index]
        if next_sell_indices:
            next_sell_index = next_sell_indices[0]
            plt.plot([data.index[buy_index], data.index[next_sell_index]], [data['Close'].iloc[buy_index], data['Close'].iloc[next_sell_index]], color='black', linestyle='--')

    for sell_index in sell_indices:
        plt.scatter(data.index[sell_index], data['Close'].iloc[sell_index], marker='v', color='red', label='Venta')

    # RSI plot
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['RSI'], label='RSI', color='orange')
    plt.axhline(y=30, color='g', linestyle='--', label='Umbral de Compra (30)')
    plt.axhline(y=70, color='r', linestyle='--', label='Umbral de Venta (70)')
    plt.title('Índice de Fuerza Relativa (RSI)')
    plt.xlabel('Fecha y Hora')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()
