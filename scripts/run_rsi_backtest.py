from src.downloader import get_hourly_data
from src.indicators import ema, rsi, atr
from src.signals import generate_signals
from src.backtest import run_backtest, export_results
from src.plot import plot_trades
import pandas as pd

df = get_hourly_data("QQQ")
df['EMA_20'] = ema(df)
df['RSI'] = rsi(df)

atr_result = atr(df)
if isinstance(atr_result, pd.DataFrame):
    df['ATR'] = atr_result['ATR']
else:
    df['ATR'] = atr_result

df = generate_signals(df)
results = run_backtest(df)
total_return = ((results['PnL'].dropna().astype(float) + 1).prod() - 1)
print(f"Összesített hozam: {float(total_return) * 100:.2f}%")
export_results(results)
df_recent = df.tail(300).copy()
df_recent.index.name = 'Date'
df_recent.index = pd.to_datetime(df_recent.index)
recent_trades = results[results['Timestamp'] >= df_recent.index[0]]
plot_trades(df_recent[['Open', 'High', 'Low', 'Close']], recent_trades)