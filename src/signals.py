def generate_signals(df, atr_mult_sl=1.0, atr_mult_tp=2.0):
    df['Signal'] = 0
    df.loc[df['RSI'] < 30, 'Signal'] = 1
    df.loc[df['RSI'] > 70, 'Signal'] = -1
    atr = df['ATR']
    if hasattr(atr, 'columns'):
        atr = atr.squeeze()
    df['SL'] = df['Close'] - atr * atr_mult_sl
    df['TP'] = df['Close'] + atr * atr_mult_tp
    return df