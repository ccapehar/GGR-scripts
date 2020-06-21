
##A short script for merging excel worksheets.

_author_ = '''Christian Capehart'''


import pandas as pd
from openpyxl import load_workbook
import numpy as np

##from glob import glob

path = 'Kam Kotia_2017, 2018-Cations&Anions_Merge - Copy (2).xlsx'

df = pd.read_excel(path, header=None)

df2 = df[11:]

##print(df2)

#combine 'column names' row and 'units' row

df3 = df.loc[10:11]

combined = df3.loc[11, 4:]+'_'+ df3.loc[10, 4:]

df3.loc[[11], 4:] = combined.values

header = df3.loc[11]

##print(type(combined))

##combine = combined.combine_first(df3.loc)

##df3.merge(combined.to_frame(), left_index=True, right_index=True)

##print(combined.to_frame())


print(header)

##for i in range(len(df3.columns)):
##    print(df3.loc[10, i])



##array = df3.to_numpy()
##
##units = array[0]
##
##print(units)
##
##column_names = array[1]
##
##print(column_names)
##
##combined = np.char.add(units, column_names)
##
##print(combined)

##a = df[10:11]
##
##b = df[11:12]
##
##print(a, b)
##
##print(b.add(a))



##for row1, row2 in df3.iterrows():
##    print(row1)
##    print(row2)
##    print(row1+row2)
##
###make it the header for the data





#Insert the metadata

#do the same thing to the other sheets and combine



new_col_list = df.iloc[:8,0].unique()

new_val_list = df.iloc[:8,1].unique()

##print(len(df.index))

for col, val in zip(reversed(new_col_list), reversed(new_val_list)):
##    print(col)
    edited_col = col.replace(":", "")
##    print(edited_col)
##    print(val)
    df2.insert(4, column=edited_col, value = range(len(df2.index)))
    df2[edited_col] = val

print(df2.iloc[:,2:5])
##
####print(df3.groupby(level=[0]).apply(','.join).reset_index())
    

##df2.insert(loc=1, column=col, 

##for name, values in df.iteritems():
##    print(name, values)




##sheets_dict = pd.read_excel(path, header=None, sheet_name=None)
##
####print(len(sheets_dict))
##
##
####for i in len(sheets_dict):
####    data = pd.read_excel('Kam Kotia_2017, 2018-Cations&Anions_Merge.xlsx', header=None)[:12]
######    print(data)
####    df = df.append(data)
####
####print(df)
##
##for sheets in sheets_dict.items():
##    data = sheets[1][12:]
####    print(data)
##    df = df.append(data) #ignore_index=True)
##
##df.reset_index(inplace=True, drop=True)
##
##print(df)
##
##book = load_workbook(path)
##writer = pd.ExcelWriter(path, engine = 'openpyxl')
##writer.book = book
##
##df.to_excel(writer, sheet_name='all_data', header=False, index=False)
##
##writer.save()
##writer.close()

##    print(sheets)


##df = pd.read_excel('Kam Kotia_2017, 2018-Cations&Anions_Merge.xlsx', set_index=False).drop(
##
####df2 = df.to_pickle('temp.pkl')
##
##df=df.drop(df.index[:10])
##
##
##
##print(df)
##

##df = pd.read_excel('Kam Kotia_2017, 2018-Cations&Anions_Merge.xlsx', header=11, index_col=1)


##'Date of sampling'



##df2 = pd.read_excel('Kam Kotia_2017, 2018-Cations&Anions_Merge.xlsx', header=None)[12:]
##
##df3 = df.append(df2)
##
##print(df)
##
##print(df2)
##
##print(df3)
