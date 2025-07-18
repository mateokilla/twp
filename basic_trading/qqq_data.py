# qqq_data.py

import yfinance as yf
import pandas as pd
import os
import matplotlib.pyplot as plt

def get_qqq_data(start='2013-01-01', end='2025-01-01'):
    qqq = yf.download('QQQ', start=start, end=end)
    close_data = qqq[['Close']].copy()
    close_data.reset_index(inplace=True)
    close_data.columns = ['Date', 'Close']
    return close_data

if __name__ == "__main__":
    data = get_qqq_data()
    
    # Mentés CSV-be
    csv_path = os.path.join(os.getcwd(), 'qqq_close_data.csv')
    data.to_csv(csv_path, index=False)

    # Ábrázolás mentése fájlba (mert Codespace nem tud megjeleníteni ablakot)
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], linewidth=1.5)
    plt.title('QQQ Záróárfolyamok')
    plt.xlabel('Dátum')
    plt.ylabel('Záró ár (USD)')
    plt.grid(True)
    plt.tight_layout()

    # Kép mentése
    image_path = os.path.join(os.getcwd(), 'qqq_chart.png')
    plt.savefig(image_path)
