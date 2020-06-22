'playing around with vectorization'

import pandas as pd

df = pd.read_excel('test.xlsx', header=None)

print(df)

def function(x):
    if type(x) is not str:
        # x = 'good input'
        return x
    elif '< ' not in x:
        x = ''
        return x 
    else:
        x = x.replace('< ', '')
        x = float(x)
        x =  x/2
        return x

df = df.applymap(function)

print(df)