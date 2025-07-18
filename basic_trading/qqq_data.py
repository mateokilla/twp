# qqq_data.py

import yfinance as yf
import pandas as pd
import os

def get_qqq_data(start='2020-01-01', end='2025-07-17'):
    qqq = yf.download('QQQ', start=start, end=end)
    close_data = qqq[['Close']].copy()
    close_data.reset_index(inplace=True)
    close_data.columns = ['Date', 'Close']
    return close_data

if __name__ == "__main__":
    data = get_qqq_data()
    csv_path = os.path.join(os.getcwd(), 'qqq_close_data.csv')
    data.to_csv(csv_path, index=False)
