import pandas as pd 

path = 'Detour 2012-2019 date formatxls.xls'

df = pd.read_excel(path, header=None)

df[1] = df[1].dt.strftime('%m/%d/%Y')

print(df)

df.to_excel('Detour 2012-2019 date formatxls Christian.xlsx', index=False, header=None)