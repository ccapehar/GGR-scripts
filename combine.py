import pandas as pd

master_file = "Combined_Unedited.xlsx"

file_to_add = r'''Joy's_to_combine.xlsx'''

df_to_combine = pd.read_excel(file_to_add, ignore_index=True)

df_master = pd.read_excel(master_file, ignore_index=True)

df_master = df_master.append(df_to_combine, ignore_index=True) 

df_master.to_excel("Combined_both_Laura_and_Joy.xlsx", index=False)