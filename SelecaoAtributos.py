# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:00:58 2021

@author: ramon
"""

#Selecao de Atributos - Modulo 31
#Vamos separar os atributos mais relevantes para a classificacao

import pandas as pd
from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier

################################################################################

#Abro o arquivo CSV

credito = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/Credit.csv') #Abro o dataset com os dados para aprendizado

print(credito.shape)
print(credito.head())

#Vamos criar uma matriz separada para as categorias e para a classe final

categorias = credito.iloc[:,0:20].values #Pego todas as linhas e colunas de 0 a 19 e transformo em matriz
classes = credito.iloc[:,20] #Pego todas as linhas da coluna 20 e transformo em matriz

print(classes)

################################################################################

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

print(x_teste)
print(y_teste)

################################################################################

#Vamos criar e treinar o modelo SVM

svm = SVC() #Maquina de Vetor de Suporte
svm.fit(x_treinamento, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

################################################################################

#Agora podemos testar o modelo na pratica

previsao = svm.predict(x_teste) #Usamos os dados das categorias do teste

print(previsao)

################################################################################

#Agora vamos analisar a taxa de acertos do modelo

taxa_acerto = accuracy_score(y_teste, previsao)

print(taxa_acerto)

################################################################################

#Vamos extrair as categorias mais importantes 

forest = ExtraTreesClassifier()
forest.fit(x_treinamento, y_treinamento)

importancias = forest.feature_importances_

print(importancias)

################################################################################

#Criando nova base de dados usando um novo x_treinamento (x = categorias) com apenas as categorias relevantes

x_treinamento2 = x_treinamento[:,[0,1,2,4]]
x_teste2 = x_teste[:,[0,1,2,4]]

################################################################################

#Vamos criar e treinar o novo modelo SVM

svm2 = SVC() #Maquina de Vetor de Suporte
svm2.fit(x_treinamento2, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

################################################################################

#Agora podemos testar o novo modelo na pratica

previsao2 = svm2.predict(x_teste2) #Usamos os dados das categorias do teste

print(previsao2)

################################################################################

#Agora vamos analisar a taxa de acertos do modelo

taxa_acerto2 = accuracy_score(y_teste, previsao2)

print(taxa_acerto2)