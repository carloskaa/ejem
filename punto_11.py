# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:15:06 2023

@author: Asus
"""
import pandas as pd
import numpy as np
from datetime import datetime ### importacion libreria para sacar fecha actual


# def fun(value):
#     if value < div:
#         return 1
#     if div <= value < div*2:
#         return 2
#     elif div*2 <= value < div*3:
#         return 3
#     elif div*3 <= value < div*4:
#         return 4
#     elif value >= div*4:
#         return 5
    
df = pd.read_csv('depositos_oinks.csv', index_col=0)  
df_2 = pd.pivot_table(df, values=['operation_value','maplocation_name','user_createddate'],index=['user_id'], aggfunc={'operation_value': np.sum,'maplocation_name':'count','user_createddate':'first'})
df_2['user_createddate'] = df_2[['user_createddate']].apply(pd.to_datetime)
df_2['Dias desde creacion'] = (datetime.now() - df_2['user_createddate'] ).dt.days
df_2 = df_2.rename(columns={'maplocation_name': "Numero de operaciones", 'user_createddate': "Fecha de creacion",'operation_value':'Cantidad total de dinero ingresado'})

df_2['quartiles Cantidad dinero'] = pd.qcut(df_2['Cantidad total de dinero ingresado'], 10, labels=False,duplicates='drop')
df_2['quartiles Dias desde creacion'] = pd.qcut(df_2['Dias desde creacion'], 10, labels=False,duplicates='drop')
df_2['quartiles Numero de operaciones'] = pd.qcut(df_2['Numero de operaciones'], 10, labels=False,duplicates='drop')
# df_2['quartiles Cantidad dinero'] = pd.qcut(df_2['Cantidad total de dinero ingresado'], 10, labels=False)
# div = max(df_2['Cantidad total de dinero ingresado'])/5
# df_2['Grupo dinero invertido'] = df_2['Cantidad total de dinero ingresado'].apply(fun)


# div = max(df_2['Numero de operaciones'])/5
# df_2['Grupo numero de operaciones'] = df_2['Numero de operaciones'].apply(fun)
# div = max(df_2['Dias desde creacion'])/5
# df_2['Grupo Dias desde creacion'] = df_2['Dias desde creacion'].apply(fun)
# df_2['Metrica de creacion'] =  (df_2['Grupo dinero invertido']*df_2['Grupo numero de operaciones'])/df_2['Grupo Dias desde creacion']
