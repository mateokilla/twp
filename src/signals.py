import pandas as pd

def generate_signals(df, atr_col='ATR', atr_mult_sl=2, atr_mult_tp=4):
    """
    Belépési/kilépési szignálok és stop-loss/take-profit szintek generálása.
    """
    # ATR oszlop biztosítása, hogy Series legyen
    atr = df[atr_col]
    if isinstance(atr, pd.DataFrame):
        # Ha DataFrame, válaszd ki az ATR oszlopot és alakítsd Series-szé
        if 'ATR' in atr.columns:
            atr = atr['ATR'].squeeze()
        else:
            atr = atr.squeeze()
    else:
        atr = atr.squeeze()

    # Stop-loss és take-profit szintek
    df["SL"] = df["Close"] - atr * atr_mult_sl
    df["TP"] = df["Close"] + atr * atr_mult_tp

    # Példa szignál logika: RSI alapján
    df["Signal"] = 0
    df.loc[df["RSI"] < 30, "Signal"] = 1   # vételi szignál
    df.loc[df["RSI"] > 70, "Signal"] = -1  # eladási szignál

    # Belépési/kilépési időpontok
    df["Entry"] = df["Signal"].shift(1).where(df["Signal"].shift(1) == 1)
    df["Exit"] = df["Signal"].shift(1).where(df["Signal"].shift(1) == -1)

    return df