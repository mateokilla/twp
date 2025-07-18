import pandas as pd

def generate_signals(df, atr_col='ATR'):
    """
    Belépési/kilépési szignálok RSI alapján.
    """
    # RSI alapú szignálok
    df["Signal"] = 0
    df.loc[df["RSI"] < 30, "Signal"] = 1   # vételi szignál
    df.loc[df["RSI"] > 70, "Signal"] = -1  # eladási szignál

    # Belépési/kilépési időpontok
    df["Entry"] = df["Signal"].shift(1).where(df["Signal"].shift(1) == 1)
    df["Exit"] = df["Signal"].shift(1).where(df["Signal"].shift(1) == -1)

    return df