import pandas as pd
df=pd.read_csv('2salary.csv')

description=df['Salary'].describe()
quantile=df['Salary'].quantile()
skewness=df['Salary'].skew()
kurtosis=df['Salary'].kurt()
value_count=df['Salary'].value_counts()

print(f"Statistical Summary : \n{description}")
print(f"Quantiles : {quantile}")
print(f"Skewness : {skewness}")
print(f"Kurtosis : {kurtosis}")
print(f"Value Counts : {value_count}")
