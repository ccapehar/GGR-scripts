# test.py

import pandas as pd 
import glob

# df3 = pd.read_pickle('temp02.pkl')

# df4 = pd.read_pickle('temp03.pkl')

# df5 = pd.read_pickle('temp04.pkl')


# cols=pd.Series(df4.columns)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(cols)

# duplicate = df5.loc[:,~df5.columns.duplicated()]

# print(duplicate)
# columns1 = list(df4.columns.values)

# columns2 = list(df5.columns.values)

# print(columns1)

# print(columns2)

files = glob.glob('temp*')

print(files)

df_to_concat = pd.DataFrame()

count = 0
for i in files:
    print(count)
    count += 1
    try:
        df_to_concat = df_to_concat.append(pd.read_pickle(i))
    except: # duplicated columns may cause an error, must rename columns
        df_with_dupes = pd.read_pickle(i)
        cols=pd.Series(df_with_dupes.columns)
        for dup in cols[cols.duplicated()].unique(): 
            cols[cols[cols == dup].index.values.tolist()] = [dup + '.' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
        df_with_dupes.columns=cols
        df_to_concat = df_to_concat.append(df_with_dupes)
    print(df_to_concat)

df_to_concat.to_excel('LL2018--Cations&Anions_Database_Format.xlsx', index=False)




# print(df)

# df = pd.read_excel('LL2018--Cations&Anions.xlsx', header=None)

# vals = list(df.iloc[:8,1].values)
# print(vals)
# index = range(len(df.index))

# df_to_insert = pd.DataFrame(index=index, columns=['Project', 'Submission', 
#     'Submitted by', 'Analysis', 'Date of Analysis', 
#     'Analyst ', 'Work #'])

# cols = list(df_to_insert.columns)

# count = 0
# for i, j in zip(cols, vals):
#     df_to_insert[i] = j
#     df.insert(4, column=i, value = range(len(df.index)))

# print(df)
