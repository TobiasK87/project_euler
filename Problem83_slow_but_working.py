# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 17:16:19 2021

@author: Tobi
"""

import pandas as pd

df = pd.read_csv(r"C:\Users\Tobi\Programmieren\Python Scripts\Project Euler\Data\Problem81_Input.csv", dtype=int, delimiter=',', header=None)

# inital guess
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

def valid(x,s):
    return min(max(0,x),s)

def refine_path(df, df_guess):
    df2 = df.copy()
    s = df.shape[0] - 1
    for i in range(df.shape[0]):
        for j in range(df.shape[0]):
            if i==0 and j==0:
                continue
            m = 10**7
            if i>0:
                m = min(m, df_guess.iloc[i-1,j])
            if i<s:
                m = min(m, df_guess.iloc[i+1,j])
            if j>0:
                m = min(m, df_guess.iloc[i,j-1])
            if j<s:
                m = min(m, df_guess.iloc[i,j+1])
            df2.iloc[i,j] = df.iloc[i,j] + m
    print((df2<df_guess).sum(axis=1), " Verbesserungen erzielt")
    return df2

while True:
    df_res_old = df_res.copy()
    df_res = refine_path(df, df_res)
    print((df_res_old!=df_res).sum(axis=1).sum())
    if (df_res_old!=df_res).sum(axis=1).sum()==0:
        break


df_res.iloc[-1,-1] # 425185