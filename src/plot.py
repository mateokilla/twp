import mplfinance as mpf
import pandas as pd
import os

def plot_trades(df_price: pd.DataFrame, trades: pd.DataFrame, filename="trade_chart.png"):
    df = df_price.copy()
    buy_signals = trades[['Timestamp', 'Entry']].dropna().set_index('Timestamp')
    sell_signals = trades[['Exit', 'Exit_Price']].dropna().set_index('Exit')
    apds = []

    if not buy_signals.empty:
        apds.append(mpf.make_addplot(buy_signals['Entry'], type='scatter', markersize=50, marker='^', color='green'))

    if not sell_signals.empty:
        apds.append(mpf.make_addplot(sell_signals['Exit_Price'], type='scatter', markersize=50, marker='v', color='red'))

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