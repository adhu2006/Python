import pandas as pd
data={'Product Name':['Deodorant','Laptop','Lays Chips'],
      'Category':['Cosmetics','Electronics','Groceries'],
      'Price':[200,80000,30]
}
df=pd.DataFrame(data)
print(f"The Original DataFrame : \n{df}")
print()
df['Discounted Price']=0.9*df['Price']
print(f"The DataFrame after modification : \n{df}")
