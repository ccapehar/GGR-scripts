import pandas as pd
from natsort import natsort, humansorted, ns
import locale
import re


# def atoi(text):
#     return int(text) if text.isdigit() else text

# def natural_keys(text):
#     '''
#     alist.sort(key=natural_keys) sorts in human order
#     http://nedbatchelder.com/blog/200712/human_sorting.html
#     (See Toothy's implementation in the comments)
#     '''
#     return [atoi(c) for c in re.split(r'(\d+)', text)]

# def alphabet(string):
#     filter(lambda x: x.isalpha(), string)
# def _human_key(key):
#     parts = re.split('(\d*\.\d+|\d+)', key)
#     return tuple((e.swapcase() if i % 2 == 0 else float(e))
#             for i, e in enumerate(parts))

# def human_keys(astr):
#     '''
#     alist.sort(key=human_keys) sorts in human order
#     '''
#     keys=[]
#     for elt in re.split('(\d+)', astr):
#         elt=elt.swapcase()
#         try: elt=int(elt)
#         except ValueError: pass
#         keys.append(elt)
#     return keys

def alph_key(x):
    alph = str.lower(str("".join(filter(lambda x: not x.isdigit(), x))))
    return alph

df = pd.read_excel("Copy of 2018_2019 All Lysim Data_20200623.xlsx", sheet_name="2019 Cations")

# print(list(df.iloc[:, 4:].columns))

df1 = df.iloc[:, 4:]
df2 = df.iloc[:, :4]

old_columns = list(df1.columns)

# locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

new_columns = sorted(old_columns, key=alph_key)

print(new_columns)

# print(natsort.natsorted(old_columns, alg=ns.LOCALE))

# print(type(list(df1.columns))