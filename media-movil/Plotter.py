import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class Plotter:
    @staticmethod
    def plot_signals(btcusdt_df, short_ma, long_ma, trend):
        plt.figure(figsize=(12, 6))

        # Línea de precio con un tono de gris oscuro
        plt.plot(btcusdt_df.index, btcusdt_df['Close'], label='Precio', color='slategray', linewidth=2)

        # Medias móviles con diferentes estilos y tonos de gris
        plt.plot(btcusdt_df.index, short_ma, label='MA short', color='darkgray', linestyle='-', linewidth=1.5)
        plt.plot(btcusdt_df.index, long_ma, label='MA long', color='lightgray', linestyle='--', linewidth=1.5)

        # Color background based on trend
        for i in range(1, len(btcusdt_df)):
            if trend[i] == 'Bullish':
                plt.axvspan(btcusdt_df.index[i-1], btcusdt_df.index[i], color='palegreen', alpha=0.1)
            elif trend[i] == 'Bearish':
                plt.axvspan(btcusdt_df.index[i-1], btcusdt_df.index[i], color='lightcoral', alpha=0.1)
            else:
                plt.axvspan(btcusdt_df.index[i-1], btcusdt_df.index[i], color='lightyellow', alpha=0.1)

        plt.scatter(btcusdt_df[btcusdt_df['Signal'] == 'BUY'].index,
                    btcusdt_df[btcusdt_df['Signal'] == 'BUY']['Close'],
                    marker='^', color='limegreen', label='Compra')
        plt.scatter(btcusdt_df[btcusdt_df['Signal'] == 'SELL'].index,
                    btcusdt_df[btcusdt_df['Signal'] == 'SELL']['Close'],
                    marker='v', color='tomato', label='Venta')
        plt.scatter(btcusdt_df[btcusdt_df['Signal'] == 'STOP_LOSS_LONG'].index,
                    btcusdt_df[btcusdt_df['Signal'] == 'STOP_LOSS_LONG']['Close'],
                    marker='x', color='black', label='Stop Loss')
        plt.scatter(btcusdt_df[btcusdt_df['Signal'] == 'SELL_SHORT'].index,
                    btcusdt_df[btcusdt_df['Signal'] == 'SELL_SHORT']['Close'],
                    marker='v', color='orange', label='Venta Corta')
        plt.scatter(btcusdt_df[btcusdt_df['Signal'] == 'COVER_SHORT'].index,
                    btcusdt_df[btcusdt_df['Signal'] == 'COVER_SHORT']['Close'],
                    marker='^', color='violet', label='Cubrimiento Corto')

        # Agregar líneas diagonales que conecten compras con ventas y ventas cortas con cubrimientos
        previous_buy_index = None
        previous_sell_short_index = None
        for i in range(len(btcusdt_df)):
            if btcusdt_df['Signal'].iloc[i] == 'BUY':
                previous_buy_index = i
            elif btcusdt_df['Signal'].iloc[i] == 'SELL' and previous_buy_index is not None:
                plt.plot([btcusdt_df.index[previous_buy_index], btcusdt_df.index[i]],
                         [btcusdt_df['Close'].iloc[previous_buy_index], btcusdt_df['Close'].iloc[i]],
                         color='limegreen', linestyle='--')
                previous_buy_index = None
            elif btcusdt_df['Signal'].iloc[i] == 'STOP_LOSS_LONG' and previous_buy_index is not None:
                plt.scatter(btcusdt_df.index[i], btcusdt_df['Close'].iloc[i], marker='x', color='black')
                previous_buy_index = None
            elif btcusdt_df['Signal'].iloc[i] == 'SELL_SHORT':
                previous_sell_short_index = i
            elif btcusdt_df['Signal'].iloc[i] == 'COVER_SHORT' and previous_sell_short_index is not None:
                plt.plot([btcusdt_df.index[previous_sell_short_index], btcusdt_df.index[i]],
                         [btcusdt_df['Close'].iloc[previous_sell_short_index], btcusdt_df['Close'].iloc[i]],
                         color='orange', linestyle='--')
                previous_sell_short_index = None
            elif btcusdt_df['Signal'].iloc[i] == 'STOP_LOSS_SHORT' and previous_sell_short_index is not None:
                plt.scatter(btcusdt_df.index[i], btcusdt_df['Close'].iloc[i], marker='x', color='black')
                previous_sell_short_index = None

        plt.title('Precio con Medias Móviles')
        plt.xlabel('Fecha y Hora')
        plt.ylabel('Precio')
        plt.legend()
        plt.grid(True)
        plt.savefig("btcusdt_chart.pdf")
        plt.show()

    @staticmethod
    def save_to_pdf(btcusdt_df, short_ma, long_ma, trend, file_path):
        with PdfPages(file_path) as pdf:
            Plotter.plot_signals(btcusdt_df, short_ma, long_ma, trend)
            pdf.savefig()  # Save the current figure into a pdf page
            plt.close()  # Close the plot to clean up memory
