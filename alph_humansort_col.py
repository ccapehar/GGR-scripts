import pandas as pd

def alph_key(x):
    alph = str.lower(str("".join(filter(lambda x: not x.isdigit(), x))))
    return alph

df = pd.read_excel("Copy of 2018_2019 All Lysim Data_20200623.xlsx", sheet_name="2019 Cations")

df1 = df.iloc[:, 4:]
df2 = df.iloc[:, :4]

unchanged_columns = list(df2.columns)

old_columns = list(df1.columns)

sorted_columns = sorted(old_columns, key=alph_key)

new_columns = unchanged_columns+sorted_columns

df = df.reindex(columns=new_columns)

print(df)

df.to_excel('temp.xlsx', index=False)