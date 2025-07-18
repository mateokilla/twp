import pandas as pd

def run_backtest(df):
    position = 0
    entry_price = 0
    sl = 0
    tp = 0
    results = []

    for i in range(1, len(df)):
        row = df.iloc[i]
        prev = df.iloc[i - 1]

        if prev['Signal'] == 1 and position == 0:
            position = 1
            entry_price = prev['Close']
            sl = prev['SL']
            tp = prev['TP']
            results.append({
                'Timestamp': prev.name,
                'Entry': entry_price,
                'SL': sl,
                'TP': tp,
                'Exit': None,
                'Exit_Price': None,
                'PnL': None
            })

        elif position == 1:
            hit_tp = row['High'] >= tp
            hit_sl = row['Low'] <= sl
            if hit_tp or hit_sl or row['Signal'] == -1:
                exit_price = tp if hit_tp else (sl if hit_sl else row['Close'])
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