# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:59:00 2021

@author: ramon
"""

#Classificador Naive Bayes - Modulo 31

import pandas as pd
from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.naive_bayes import GaussianNB #Utilizamos o Naive Bayes
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from yellowbrick.classifier import ConfusionMatrix

credito = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/Credit.csv')

print(credito.shape)
print(credito.head())

#Vamos criar uma matriz separada para as categorias e para a classe final

categorias = credito.iloc[:,0:20].values #Pego todas as linhas e colunas de 0 a 19 e transformo em matriz
classes = credito.iloc[:,20] #Pego todas as linhas da coluna 20 e transformo em matriz

print(classes)


#######################################################################################

#Naive Bayes tem problemas com dados categoricos
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

#Vamos criar e treinar o modelo Naive_Bayes

naive_bayes = GaussianNB()
naive_bayes.fit(x_treinamento, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

################################################################################

#Agora podemos testar o modelo na pratica

previsao = naive_bayes.predict(x_teste) #Usamos os dados das categorias do teste

print(previsao)

################################################################################

#Agora vamos analisar a taxa de erros e acertos do modelo, atraves da matriz de confusao

confusao = confusion_matrix(y_teste, previsao)
print(confusao)

#Utilizamos tambem o accuracy para determinar a taxa de acerto
taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print(taxa_acerto)

#Matriz de Confusao de forma Visual

v = ConfusionMatrix(GaussianNB())
v.fit(x_treinamento, y_treinamento)
v.score(x_teste, y_teste)
v.poof()

################################################################################

#Estamos satisfeitos com a eficiencia do modelo, agora, vamos fazer a predicao com dados completamente novos
#Vou abrir uma nova planilha e fazer a predicao com base no modelo

dadosnovos = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/NovoCredit.csv')

print(dadosnovos.head())

################################################################################

#Vou ter que substituir as colunas categoricas por numericas novamente

categoriasnovas = dadosnovos.iloc[:,0:20].values #Pego todas as categorias da coluna 0 a 19

#Reutilizo os LabelEncoders utilizados anteriormente
categoriasnovas[:,0] = labelencoder1.fit_transform(categoriasnovas[:,0])
categoriasnovas[:,2] = labelencoder2.fit_transform(categoriasnovas[:,2])
categoriasnovas[:,3] = labelencoder3.fit_transform(categoriasnovas[:,3])
categoriasnovas[:,5] = labelencoder4.fit_transform(categoriasnovas[:,5])
categoriasnovas[:,6] = labelencoder5.fit_transform(categoriasnovas[:,6])
categoriasnovas[:,8] = labelencoder6.fit_transform(categoriasnovas[:,8])
categoriasnovas[:,9] = labelencoder7.fit_transform(categoriasnovas[:,9])
categoriasnovas[:,11] = labelencoder8.fit_transform(categoriasnovas[:,11])
categoriasnovas[:,13] = labelencoder9.fit_transform(categoriasnovas[:,13])
categoriasnovas[:,14] = labelencoder10.fit_transform(categoriasnovas[:,14])
categoriasnovas[:,16] = labelencoder11.fit_transform(categoriasnovas[:,16])
categoriasnovas[:,18] = labelencoder12.fit_transform(categoriasnovas[:,18])
categoriasnovas[:,19] = labelencoder13.fit_transform(categoriasnovas[:,19])

#Uso o modelo Naive_Bayes para fazer a predicao das novas categorias

resultado = naive_bayes.predict(categoriasnovas) 
print(resultado)