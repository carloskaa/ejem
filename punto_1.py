# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:15:06 2023

@author: Asus
"""
import pandas as pd ### importacion libreria para analisis de datos
import numpy as np ## importacion libreia analisis numerico
from datetime import datetime ### importacion libreria para sacar fecha actual
    
df = pd.read_csv('depositos_oinks.csv', index_col=0)  ### lectura archivo
df_2 = pd.pivot_table(df, values=['operation_value','maplocation_name','user_createddate'],index=['user_id'], aggfunc={'operation_value': np.sum,'maplocation_name':'count','user_createddate':'first'}) ## creacion tabla de datos de interes por usuario 
df_2['user_createddate'] = df_2[['user_createddate']].apply(pd.to_datetime) ## cambiar formato a fecha
df_2['Dias desde creacion'] = (datetime.now() - df_2['user_createddate'] ).dt.days ## calcular numero de dias desde su creacion a hoy
df_2 = df_2.rename(columns={'maplocation_name': "Numero de operaciones", 'user_createddate': "Fecha de creacion",'operation_value':'Cantidad total de dinero ingresado'}) ##cambiar nombre columnas

df_2['Quartiles Cantidad dinero'] = pd.qcut(df_2['Cantidad total de dinero ingresado'], 10, labels=False,duplicates='drop') ##crear nueva columna usando una division de 10 cuartiles 
df_2['Quartiles Dias desde creacion'] = pd.qcut(df_2['Dias desde creacion'], 10, labels=False,duplicates='drop') ##crear nueva columna usando una division de 10 cuartiles 
df_2['Quartiles Numero de operaciones'] = pd.qcut(df_2['Numero de operaciones'], 10, labels=False,duplicates='drop') ##crear nueva columna usando una division de 10 cuartiles 

df_2['Metrica de creacion'] =  ((df_2['Quartiles Cantidad dinero']+1)*(df_2['Quartiles Numero de operaciones']+1))/(df_2['Quartiles Dias desde creacion']+1) ##creacion metrica de puntcion con la formula que defini
df_2['Quartiles Metrica de creacion'] = pd.qcut(df_2['Metrica de creacion'], 10, labels=False,duplicates='drop') ##creacion de 10 cuartiles para la metrica de evaluacion
df_2['Quartiles Metrica de creacion'] = (df_2['Quartiles Metrica de creacion']+1)/2 ## estandarizacion de 1-5 de la metrica en cuartiles, este columna es la calificacion de cada usuario