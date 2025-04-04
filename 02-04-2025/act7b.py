import pandas as pd
df=pd.read_csv('6Mcd_null_values.csv')
print(f"After filling all the null values : \n{df.fillna(0)}")
print(f"After dropping duplicates :\n{df.drop_duplicates()}")
