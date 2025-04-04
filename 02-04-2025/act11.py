import pandas as pd
df=pd.read_csv('3Salary_Data.csv')

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaled_data=scaler.fit_transform(df)
scaled_df1=pd.DataFrame(scaled_data,columns=df.columns)
scaled_df1
