"records the files"
import pandas as pd
import os
import datetime
  
name_of_list = 'log_of_combined_files.xlsx'
filename_addition = '_Database_Format'
original_author = 'Joy Hu'
current_date = datetime.datetime.today()
new_log = []
path = os.getcwd()



for root, dirs, files in os.walk(path):
    for file in files:
        if 'Cations&Anions' in file:
            if filename_addition in file:
                log_file = file.replace(filename_addition, '')
                new_log.append(log_file)

df_to_append = pd.DataFrame(new_log, columns=['Combined Files'])

df_to_append.insert(1, column='Date', value = range(len(df_to_append.index)))
df_to_append['Date'] = current_date
df_to_append.insert(2, column='Author', value = range(len(df_to_append.index)))
df_to_append['Author'] = original_author



print(df_to_append)
df_log = pd.read_excel(name_of_list, index=False)

df_log = df_log.append(df_to_append)

df_log.to_excel(name_of_list, index=False)

