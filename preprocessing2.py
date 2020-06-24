import pandas as pd 
from glob import glob

def format(df, cnt): #formats the dataframe into a database friendly format
    df2 = df.loc[11:]
    df3 = df.loc[10:11]

    combined = df3.loc[11, 4:]+' '+ df3.loc[10, 4:] 

    df3.loc[[11], 4:] = combined.values

    header = df3.loc[11]

    df4 = df.loc[12:]
    df4.columns = header

    # new_col_list = ['Report', 'Project', 'Submission', 
    # 'Submitted by', 'Analysis', 'Date of Analysis', 
    # 'Analyst ', 'Work #']

    # new_val_list = list(df.iloc[:8,1].values)

    # for col, val in zip(reversed(new_col_list), reversed(new_val_list)):
    #     edited_col = col.replace(":", "")
    #     df4.insert(4, column=edited_col, value = range(len(df4.index)))
    #     df4[edited_col] = val
    
    print(df4)

    df4.to_pickle(f'temp{cnt:02d}.pkl')

def make_new_excel_file(file, filename_addition): #generates an excel file from sheets
    sheets_dict = pd.read_excel(file, header=None, sheet_name=None)

    database_format = pd.DataFrame()

    for idx, sheets in enumerate(sheets_dict.items()):
        if sheets[0] in {'database_format', 'database_format1', 'all_data'}: #avoiding duplicates
            continue
        data = sheets[1]
        format(data, idx)
        # temp = pd.read_pickle(f'temp{idx:02d}.pkl')
        # database_format = database_format.append(temp, ignore_index=True)
        # print(database_format)
        # print(pd.read_pickle(f'temp{idx:02d}.pkl'))


    files = glob('*.pkl')
    print(files)
    # print([pd.read_pickle(fp) for fp in files])
    database_format = pd.concat([pd.read_pickle(fp) for fp in files], ignore_index=True)
    print(database_format)

    old_filename, file_extension = os.path.splitext(file)
    new_file = old_filename+filename_addition+file_extension

    # database_format.to_excel(new_file, index=False)

    for pkl_files in glob.glob("*.pkl" ):
        os.remove(pkl_files)

file = 'LL2018--Cations&Anions.xlsx'

filename_addition = '_Database_Format'

make_new_excel_file(file, filename_addition)




# def format(df): #formats the dataframe into a database friendly format
    
#     # making the header and removing the extra info
#     df3 = df.loc[10:11]
#     combined = df3.loc[11, 4:]+' '+ df3.loc[10, 4:] 
#     df3.loc[[11], 4:] = combined.values
#     header = df3.loc[11]
#     df4 = df.loc[12:]
#     df4.columns = header

#     # inserting the extra info

#     new_col_list = ['Project', 'Submission', 
#     'Submitted by', 'Analysis', 'Date of Analysis', 
#     'Analyst ', 'Work #']

#     new_val_list = list(df.iloc[:8,1].values)

#     for col, val in zip(reversed(new_col_list), reversed(new_val_list)):
#         df4.insert(4, column=col, value = val)
#         # df4[edited_col] = val
 
#     return df4
#     # df4.to_pickle(f'temp{cnt:02d}.pkl')



df = pd.read_excel('LL2018--Cations&Anions.xlsx')

format(df)

print(df)