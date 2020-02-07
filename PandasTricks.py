# shift()

import pandas as pd 
import numpy as np 

df = pd.DataFrame({'DATE': [1, 2, 3, 4, 5],
	'VOLUMNE': [100, 200, 300, 400, 500],
	'PRICE': [214, 234, 253, 272, 291]})
print(df)
df.shift(1)
# with fill_Value = 0
df.shift(1,fill_value=0)

df['PREV_DAY_PRICE'] = df['PRICE'].shift(1,fill_value=0)
print(df)

df['LAST_3_DAYS_AVE_PRICE'] = (df['PRICE'].shift(1,fill_value=0) +
	df['PRICE'].shift(2,fill_value=0) +
	df['PRICE'].shift(2,fill_value=0)) /3

df['TOMORROW_PRICE'] = df['PRICE'].shift(-1,fill_value=0)

# value_counts()
a = pd.Index([3,3,4,2,1,3, 1, 2, 3, 4, np.nan,4,6,7])
a.value_counts()

b = pd.Series(['ab','bc','cd',1,'cd','cd','bc','ab','bc',1,2,3,2,3,np.nan,1,np.nan])
b.value_counts()

a = pd.Index([3,3,4,2,1,3, 1, 2, 3, 4, np.nan,4,6,7])
a.value_counts(bins=4)

# mask()
df = pd.DataFrame(np.arange(15).reshape(-1, 3), columns=['A', 'B','C'])
print(df)

#mask operation to check if element is divided by 2 without any remainder. If match change the sign of the element as original
df.mask(df % 2 == 0,-df)

# nlargest()
df = pd.DataFrame({'HEIGHT': [170,78,99,160,160,130,155,70,70,20],
                   'WEIGHT': [50,60,70,80,90,90,90,50,60,70]},
                   index=['A','B','C','D','E','F','G','H','I','J'])
print(df)

dfl = df.nlargest(3,'HEIGHT')
print(dfl)

# nsmallest()
df = pd.DataFrame({'HEIGHT': [170,78,99,160,160,130,155,70,70,20],
                   'WEIGHT': [50,60,70,80,90,90,90,50,60,70]},
                   index=['A','B','C','D','E','F','G','H','I','J'])
print(df)


dfs = df.nsmallest(3,'WEIGHT')
print(dfs)