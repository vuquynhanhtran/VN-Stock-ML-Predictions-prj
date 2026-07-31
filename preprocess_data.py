import pandas as pd
df = pd.read_csv('vnindex.csv', delimiter=';', encoding='utf-8', header=1)
df.columns = [
    'Date', 'Close', 'Adjusted_close', 'DropMe', 'Volume', 'Trading_Value',
    'Volume_2', 'Trading_Value_2', 'Open', 'High', 'Low'
]

df = df.drop(columns=['DropMe'])
df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%y')

num_cols = ['Close', 'Adjusted_close', 'Volume', 'Trading_Value',
            'Volume_2', 'Trading_Value_2', 'Open', 'High', 'Low']
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(',', '').replace('nan', None).astype(float)

df = df.sort_values('Date')

cutoff1 = pd.to_datetime('2025-05-01') 
cutoff2 = pd.to_datetime('2025-06-26')  

train_df = df[df['Date'] < cutoff1]
validation_df = df[(df['Date'] >= cutoff1) & (df['Date'] < cutoff2)]
test_df = df[df['Date'] >= cutoff2]

print("Train set:", train_df['Date'].min(), "→", train_df['Date'].max())
print('Validation set', validation_df['Date'].min(), "→", validation_df['Date'].max())
print("Test set:", test_df['Date'].min(), "→", test_df['Date'].max())
print("Train size:", len(train_df),"Validation size", len(validation_df), "Test size:", len(test_df))

