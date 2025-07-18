import pandas as pd

def ema(df: pd.DataFrame, period: int = 20) -> pd.Series:
    """Exponenciális mozgóátlag (EMA)"""
    return df['Close'].ewm(span=period, adjust=False).mean()

def rsi(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """Relative Strength Index (RSI)"""
    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = -delta.clip(upper=0).rolling(period).mean()
    rs = gain / loss
    rsi_series = 100 - (100 / (1 + rs))
    return rsi_series

def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    """Average True Range (ATR)"""
    high_low = df['High'] - df['Low']
    high_close = (df['High'] - df['Close'].shift()).abs()
    low_close = (df['Low'] - df['Close'].shift()).abs()
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr_series = tr.rolling(window=period).mean()
    return atr_series