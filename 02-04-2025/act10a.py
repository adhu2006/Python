import pandas as pd
df=pd.read_csv('4laptops.csv')

#One hot encoding
d1=OneHotEncoder()
d1_data=d1.fit_transform(df[[' Storage']])
d1_array=d1_data.toarray()

d1_cols=d1.categories_

d1_df=pd.DataFrame(d1_array,columns=d1_cols)

df_final=df.join(d1_df)

print(f"DataFrame after One Hot Encoding : \n{df_final}")
#Label Encoder
df=pd.read_csv('4laptops.csv')
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
df[' Storage']=le.fit_transform(df[' Storage'])
print(f"DataFrame after using LabelEncoder : \n{df}")
