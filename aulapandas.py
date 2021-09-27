# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:40:42 2021

@author: ramon
"""

#Pandas - Modulo 8

import pandas as pd
import numpy as np

genoma = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/genoma.csv')

#print(genoma.shape) #Mostra o tamanho da Matriz
#print(genoma.describe) #Mostra apenas um resumo
#print(genoma)

print(genoma.head(15)) #Mostra os primeiros 15 registros do arquivo csv e mostra todas as colunas
print(genoma.tail(10)) #Mostra os ultimos 10 registros do arquivo csv e mostra todas as colunas

#Filtrar Colunas
print(genoma[['chromosome']])
print(genoma[['chromosome']].head(15)) #Mostra os 15 primeiros registros da coluna cromossomo

#Filtrar linhas por indice
print(genoma.loc[0:30]) #Filtro da linha 0 ate a 30
print('________________________')
print(genoma.loc[[3,30]]) #Filtro a linha 3 e a 30
print('________________________')

print(genoma.loc[genoma['genotype'] == 'AA']) #Mostra todas as linhas em que a coluna genotype apresenta AA
print(genoma.loc[genoma['position'] > 800000]) #Filtro por condicoes

print(genoma[['chromosome', 'genotype']].loc[genoma['chromosome'] == 'X']) #Filtro duas colunas e filtro as linhas X
print(genoma[['chromosome', 'genotype']].loc[genoma['chromosome'] == 'X'].loc[genoma['genotype'] == 'CG']) #Filtro duas colunas e filtro as linhas X e CG

#Criar tabelas com Series
tabela1 = pd.Series([1,10,100, 454, 890])
print(tabela1)

lista1 = np.array([1,40,80,90,100,110])
tabela2 = pd.Series(lista1) #Crio uma tabela a partir de um array numpy
print(tabela2)
print('________________________________')

#Series a partir de um arquivo csv
tabela3 = genoma['genotype'] #Gero uma Serie
print(tabela3) 
print('_____')
print(type(tabela3))

tabela4 = genoma[['genotype']] #Gero um dataframe
print(tabela4)
print(type(tabela4))

#Renomeando colunas
print(genoma.rename(columns = {'genotype':'genotipo'})) #Alteracao ocorre apenas no print

genoma.rename(columns = {'genotype':'genotipo'}, inplace=True) #Alteracao permanente (nao salva no csv)
print(genoma)

#Excluir uma coluna
genoma.drop('position', axis=1, inplace=True) #Deleta a coluna position
print(genoma)

#Verificar dados nulos
print(genoma.isnull()) #Retorna True para dados nulos ou False

print(genoma.isnull().sum()) #Mostra a quantidade de nulos encontrados na tabela inteira

#Retirar dados com nulos
print(genoma.dropna())

#Preencher dados faltando
print(genoma['genotipo'].fillna(0, inplace=True)) #inplace significa tornar permanente e 0 representa o valor a ser preenchido

#Iloc
print(genoma.iloc[0:3, 0:2]) #Filtra intervalos de linhas e colunas
print(genoma.iloc[[1,4,6], 0:2]) #Filtra uma lista de linhas e um intervalo de colunas de 0 a 2




