# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:48:08 2021

@author: ramon
"""

#Random Forest - Modulo 31

#Random Forest trata-se de um conjunto de variacoes de arvores de decisao:
#Variando modelos de aprendizado, registros, atributos...


import pandas as pd
from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.preprocessing import LabelEncoder #Para transformar dados categoricos em numericos
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from sklearn.ensemble import RandomForestClassifier

#################################################################################

#Vamos aplicar a Random Forest no arquivo csv de credito

credito = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/Credit.csv')

print(credito.shape)
print(credito.head(10))

#################################################################################

#Vamos criar uma matriz separada para as categorias e para a classe final

categorias = credito.iloc[:,0:20].values #Pego todas as linhas e colunas de 0 a 19 e transformo em matriz
classes = credito.iloc[:,20] #Pego todas as linhas da coluna 20 e transformo em matriz

#######################################################################################

#Vamos transformar todas as colunas categoricas em numericas

labelencoder1 = LabelEncoder()
categorias[:,0] = labelencoder1.fit_transform(categorias[:,0])

labelencoder2 = LabelEncoder()
categorias[:,2] = labelencoder2.fit_transform(categorias[:,2])

labelencoder3 = LabelEncoder()
categorias[:,3] = labelencoder3.fit_transform(categorias[:,3])

labelencoder4 = LabelEncoder()
categorias[:,5] = labelencoder4.fit_transform(categorias[:,5])

labelencoder5 = LabelEncoder()
categorias[:,6] = labelencoder5.fit_transform(categorias[:,6])

labelencoder6 = LabelEncoder()
categorias[:,8] = labelencoder6.fit_transform(categorias[:,8])

labelencoder7 = LabelEncoder()
categorias[:,9] = labelencoder7.fit_transform(categorias[:,9])

labelencoder8 = LabelEncoder()
categorias[:,11] = labelencoder8.fit_transform(categorias[:,11])

labelencoder9 = LabelEncoder()
categorias[:,13] = labelencoder9.fit_transform(categorias[:,13])

labelencoder10 = LabelEncoder()
categorias[:,14] = labelencoder10.fit_transform(categorias[:,14])

labelencoder11 = LabelEncoder()
categorias[:,16] = labelencoder11.fit_transform(categorias[:,16])

labelencoder12 = LabelEncoder()
categorias[:,18] = labelencoder12.fit_transform(categorias[:,18])

labelencoder13 = LabelEncoder()
categorias[:,19] = labelencoder13.fit_transform(categorias[:,19])

#0,2,3,5,6,8,9,11,13,14,16,18 e 19 sao colunas categoricas, porem, agora sao numericas


################################################################################

#Agora vamos dividir os dados entre treino e teste
#Dividiremos em 70% dos dados para treino e 30% para teste

#X sao os dados das categorias e Y os dados daquilo que eu desejo prever
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(categorias, 
                                                                  classes, 
                                                                  test_size = 0.3,
                                                                  random_state = 0)
print('TREINAMENTO DO MODELO:')
print(len(x_treinamento))
print(len(x_teste))

################################################################################

#Vamos criar e treinar o modelo Random Forest

floresta = RandomForestClassifier(n_estimators = 100) #Decidimos o numero de arvores aleatorias a serem criadas
floresta.fit(x_treinamento, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

################################################################################

#Podemos visualizar os atributos das arvores de decisao

print('ATRIBUTOS [TODOS]: ', floresta.estimators_) #pegamos as configuracoes de todas as arvores
print('ATRIBUTOS [1]: ', floresta.estimators_[1]) #pegamos as configuracoes da arvore 1

################################################################################

#Agora podemos testar o modelo na pratica

previsao = floresta.predict(x_teste) #Usamos os dados das categorias do teste

print(previsao)

################################################################################

#Agora vamos analisar a taxa de erros e acertos do modelo, atraves da matriz de confusao

confusao = confusion_matrix(y_teste, previsao)
print(confusao)

#Utilizamos tambem o accuracy para determinar a taxa de acerto
taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print(taxa_acerto)

