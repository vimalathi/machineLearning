import pandas as pd
# for data sets
import quandl

df = quandl.get('WIKI/GOOGL')
#print(df.head())
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Open'] * 100.0
df['PCT_charge'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_charge', 'Adj. Volume']]

print(df.head())
