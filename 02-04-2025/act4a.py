import pandas as pd
df=pd.read_csv('1experience.csv')

print(f"1. Last 3 rows only\n{df.tail(3)}")
print("2. Description and information")
print(f"{df.describe()}")
print(df.info())

print(f"3. Column names {df.columns}")
