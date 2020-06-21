
##A short script for merging excel worksheets.

_author_ = '''Christian Capehart'''

import pandas as pd
from openpyxl import load_workbook



path = 'Kam Kotia_2017, 2018-Cations&Anions_Merge.xlsx'
df = pd.read_excel(path, header=None)[:12]
sheets_dict = pd.read_excel(path, header=None, sheet_name=None)

for sheets in sheets_dict.items():
    data = sheets[1][12:]
    df = df.append(data) 

df.reset_index(inplace=True, drop=True)

book = load_workbook(path)
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book

df.to_excel(writer, sheet_name='all_data', header=False, index=False)

writer.save()
writer.close()
