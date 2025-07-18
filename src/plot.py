import mplfinance as mpf
import pandas as pd
import os

def plot_trades(df_price: pd.DataFrame, trades: pd.DataFrame, filename="trade_chart.png"):
    df = df_price.copy()

    # Minden oszlopot alakíts át Series-é, ha nem az!
    for col in ['Open', 'High', 'Low', 'Close']:
        if not isinstance(df[col], pd.Series):
            df[col] = pd.Series(df[col])
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Dobd el azokat a sorokat, ahol bármelyik árfolyam oszlop NaN!
    df = df.dropna(subset=['Open', 'High', 'Low', 'Close'])

    buy_signals = trades[['Timestamp', 'Entry']].dropna()
    sell_signals = trades[['Exit', 'Exit_Price']].dropna()
    apds = []

    if not buy_signals.empty:
        apds.append(mpf.make_addplot(
            buy_signals.set_index('Timestamp')['Entry'],
            type='scatter', markersize=50, marker='^', color='green'
        ))

    if not sell_signals.empty:
        apds.append(mpf.make_addplot(
            sell_signals.set_index('Exit')['Exit_Price'],
            type='scatter', markersize=50, marker='v', color='red'
        ))

    os.makedirs("src/export", exist_ok=True)

    mpf.plot(
        df,
        type='candle',
        style='charles',
        addplot=apds,
        volume=False,
        title="QQQ - Backtest Trade Chart",
        ylabel='Price',
        savefig='src/export/' + filename
    )

    print(f"Chart elmentve: src/export/{filename}")