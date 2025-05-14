import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('transactions_sample.csv', header=None, parse_dates=[0])

    df.iloc[:, 2] = pd.to_numeric(df.iloc[:, 2])
    df['Month'] = df.iloc[:, 0].dt.to_period('M')

    monthly_expenses = df.groupby('Month')[df.columns[2]].sum()
    group_expenses = df.groupby(1)[df.columns[2]].sum()

    monthly_expenses.to_csv('monthly_summary.csv', header=None)

    with open('trend_analysis.txt', 'w') as f:
            f.write(group_expenses.to_string(header=False))