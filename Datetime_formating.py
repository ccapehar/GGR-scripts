"To format the date/time, may be merged into cleanup.py later"

_author_ = '''Christian Capehart'''

import pandas as pd
from datetime import datetime 

df = pd.read_excel('Laura_ICICP merge_Combined.xlsx')

x = df.loc[:, ['Date of sampling']]

x = pd.to_datetime(x.stack(), errors = 'coerce').unstack()

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(x)

