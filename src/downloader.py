import yfinance as yf
import pandas as pd

def get_hourly_data(ticker: str = "QQQ", period: str = "1y", interval: str = "1h") -> pd.DataFrame:
    df = yf.download(tickers=ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df