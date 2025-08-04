import pandas as pd

# Read file, file uses semicolons instead of commas to separate values, also ensures proper dcoding of Vietnamese 
# characters, and tell pandas the actual column names are on the second row (index 1) not the first one
df = pd.read_csv('vnindex.csv', delimiter=';', encoding='utf-8', header=1)

# Rename columns to usable names (Vietnamse has weird column names)
df.columns = [
    'Date', 'Close', 'Adjusted_close', 'DropMe', 'Volume', 'Trading_Value',
    'Volume_2', 'Trading_Value_2', 'Open', 'High', 'Low'
]

# Drop useless column, DropMe is a placeholder name for a column that contained nothing meaningful - probably 
# empty or duplicate. This line is removed in my DataFrame

df = df.drop(columns=['DropMe'])

# Convert 'Date' to datetime, into a proper datetime object. The goal is to let me sort, filter by date, and do 
# time series operations later
df["Date"] = pd.to_datetime(df["Date"], format='%d/%m/%y')

# Creating a list of columns that should be numeric. 
num_cols = ['Close', 'Adjusted_close', 'Volume', 'Trading_Value',
            'Volume_2', 'Trading_Value_2', 'Open', 'High', 'Low']
#Clean every numeric column in the list. 
    # 1 .astype(str) → Convert to string to manipulate them safely
    # 2 .str.replace(',', '') → Remove thousand separators
    # 3 .replace('nan', None) → Replace any literal 'nan' strings with actual missing value (None)
    # 4 .astype(float) → Convert it back to float so you can do math with it
for col in num_cols:
    df[col] = df[col].astype(str).str.replace(',', '').replace('nan', None).astype(float)

df = df.sort_values('Date')

cutoff1 = pd.to_datetime('2025-05-01')  # 1 May 2025
cutoff2 = pd.to_datetime('2025-06-26')  # 26 June 2025

train_df = df[df['Date'] < cutoff1]
validation_df = df[(df['Date'] >= cutoff1) & (df['Date'] < cutoff2)]
test_df = df[df['Date'] >= cutoff2]

#Print this to show the dates and the sizes of the respected csv files
print("Train set:", train_df['Date'].min(), "→", train_df['Date'].max())
print('Validation set', validation_df['Date'].min(), "→", validation_df['Date'].max())
print("Test set:", test_df['Date'].min(), "→", test_df['Date'].max())
print("Train size:", len(train_df),"Validation size", len(validation_df), "Test size:", len(test_df))

# #save as new csv files
# train_df.to_csv('train.csv', index = False)
# validation_df.to_csv('validation.csv', index = False)
# test_df.to_csv('test.csv', index = False)


