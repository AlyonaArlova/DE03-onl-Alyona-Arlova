import pandas as pd
import numpy as np
df = pd.read_csv("/Users/Alyona_Arlova/Desktop/DE03-onl-Alyona-Arlova/PYTHON/HW8/customers.csv")
print("Content of Customer file: ", df)
print("Info about Customer file: ", df.info())

print("First 3 rows: ",df.head(3)) #print first 3 rows
print("Last 3 rows: ", df.tail(3)) #print last 3 rows
print("Is duplicate row? ", df.duplicated()) #true - for duplicates
df['number_of_orders'] = np.random.randint(50, 100, size = len(df))
print("With Number_of_orders column", df)
print(df['number_of_orders'].min(), df['number_of_orders'].max(), df['number_of_orders'].median())
print(df['first_name'].value_counts())
print(df['last_name'].value_counts())
print("Average orders:", df['number_of_orders'].mean())
print(df.nlargest(5, 'number_of_orders'))
print(df.groupby('first_name')['number_of_orders'].sum())
print(df.groupby('last_name')['number_of_orders'].mean())

