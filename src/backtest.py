import pandas as pd
import os

def run_backtest(df):
    position = 0
    entry_price = 0
    results = []

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if prev['Signal'].item() == 1 and position == 0:
            position = 1
            entry_price = prev['Close']
            results.append({
                'Timestamp': prev.name,
                'Entry': entry_price,
                'Exit': None,
                'Exit_Price': None,
                'PnL': None
            })

        elif position == 1:
            if row['Signal'].item() == -1:
                exit_price = row['Close']
                pnl = (exit_price - entry_price) / entry_price
                results[-1]['Exit'] = row.name
                results[-1]['Exit_Price'] = exit_price
                results[-1]['PnL'] = pnl
                position = 0

    return pd.DataFrame(results)

def export_results(df: pd.DataFrame, filename="rsi_backtest_results.csv"):
    path = "src/export/" + filename
    df.to_csv(path, index=False)
    print(f"Eredmény elmentve: {path}")
    
def export_results(df: pd.DataFrame, filename="rsi_backtest_results.csv"):
    os.makedirs("src/export", exist_ok=True)
    # Csak a dátum és az árfolyam oszlopokat exportáld
    export_df = df[['Exit', 'Exit_Price']]
    export_df.to_csv("src/export/" + filename, index=False)
    print(f"Eredmény elmentve: src/export/{filename}")