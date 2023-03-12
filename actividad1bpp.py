#FASE DE PRUEBAS


import pandas as pd

df = pd.read_csv('finanzas2020[1].csv')

df_sumas = pd.DataFrame(columns = df.columns)


def suma(vector):
    n = len(vector)
    s = 0
    for i in 0,n-1:
        if type(vector[i]) == float:
            s = s+vector[i]
    return s

for i in range(df.shape[1]):
    for j in df.index:
        if type(df.iloc[])
'''
for i in range(df.shape[1]):
    df_sumas.iloc[0,i] = suma(df.iloc[:,i])
'''

print(df_sumas)
