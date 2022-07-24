# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:53:14 2021

@author: Tobi
"""
df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\Project Euler\Data\Problem81_Input.csv", dtype=int, delimiter=',', header=None)


def calc_path(df):
    df2 = df.copy()
    for i in range(1, df.shape[0]):
        df2.iloc[i,0] += df2.iloc[i-1,0]
    for j in range(1, df.shape[1]):
        df2.iloc[0,j] += df2.iloc[0,j-1]
    for i in range(1, df.shape[0]):
                   for j in range(1, df.shape[1]):
                       df2.iloc[i,j] += min(df2.iloc[i,j-1], df2.iloc[i-1,j])
    return df2

df_res = calc_path(df)

print(df_res.iloc[-1,-1]) # 427337