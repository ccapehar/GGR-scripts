'''This file cleans a database-formatted excel file of any duplicate rows, missing numbers, etc.
It also returns files of the variables that needed to be cleaned.
'''

_author_ = '''Christian Capehart'''

import pandas as pd
import regex

filename = 'Laura_ICICP merge_Combined'
extension = '.xlsx'
file_addition_cleaned = '_Cleaned'
file_addition_duplicate = '_Total_Duplicate_Rows'
file_addition_missing = '_Total_Missing_Values'


df = pd.read_excel(filename+extension)

sum_of_duplicate_rows = df.duplicated(list(df)).sum()
total_rows = len(df.index)

with open(filename +file_addition_duplicate+'.txt', 'w') as f:
  f.write(f'''The file "{filename}{extension}" has {sum_of_duplicate_rows} duplicate rows out of {total_rows} total rows.''')

df = df.drop_duplicates()

df = df.replace(regex='<.+', value='')
df = df.replace('O/R', '')

df.to_excel(filename+file_addition_cleaned+extension, index=False)

df = pd.read_excel(filename+file_addition_cleaned+extension)
total_missing = df.isnull().sum()

# print(total_missing)
total_missing.to_excel(filename+file_addition_missing+extension)