import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('webserver_logs.csv', header=None)

    error_mask = df.iloc[:, 3].astype(str).str.startswith(('4', '5'))

    filtered_ips = df[error_mask]

    error_counts = filtered_ips.value_counts()
    frequent_offenders = error_counts[error_counts >= 3]
    offenders_df = frequent_offenders.reset_index()

    with open('errors.txt', 'w') as f:
        f.write(filtered_ips.to_string(index=False, header=False))

    with open('blacklist.txt', 'w') as f:
        if offenders_df.empty:
            f.write('0')
        else:
            f.write(offenders_df.iloc[:, 0].to_string(index=False, header=False))