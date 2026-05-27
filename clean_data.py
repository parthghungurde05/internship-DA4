import pandas as pd
df=pd.read_csv('data/raw_sales_data.csv');df.drop_duplicates(inplace=True);df.fillna('Unknown',inplace=True);df.to_csv('cleaned_data.csv',index=False)