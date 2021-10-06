# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:34:55 2021

@author: ramon
"""

#Aprendizado Baseado Em Instancias - Modulo 31

#Nao existe a construcao de um modelo de aprendizado, as previsoes se dao por meio
#do quanto o elemento a ser previsto esta relacionado com algum dos dados passados

#Busca o registro passado que mais se aproxima com o registro novo, usando uma metrica 
#como a distancia euclidiana

#Neste exemplo, vamos usar a metrica do vizinho mais proximo (K)

from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import pandas as pd
from scipy import stats

#################################################################################

#importo um csv TEMPORARIO que classifica especies de plantas do genero Iris
plantas = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/iris.csv')

print(plantas.head(10)) #Exibo os primeiros 10 elementos da lista

#################################################################################

#Carrego os dados de Iris em uma nova variavel com todos os dados numericos
iris = datasets.load_iris() #Converte a coluna das classes de categorico para numerico (use o outro metodo)
print(stats.describe(iris.data)) #Descreve media, variancia...

#################################################################################

#Separo as colunas das categorias da coluna das classes

print('____________________________')
print(iris.data) #Coloco todos os dados em uma matriz (apenas as categorias)
print(iris.target) #Coloco todas as classes em uma matriz

categorias = iris.data
classes = iris.target

#################################################################################

#Agora vamos dividir os dados entre treino e teste
#Dividiremos em 70% dos dados para treino e 30% para teste

#X sao os dados das categorias e Y os dados daquilo que eu desejo prever
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(categorias, 
                                                                  classes, 
                                                                  test_size = 0.3,
                                                                  random_state = 0)

print('_________________________Treino e Teste')
print(len(x_treinamento)) #Numero de exemplos separados para treinamento
print(len(x_teste)) #Numero de exemplos separados para teste


#################################################################################

#Vamos criar e treinar o modelo baseado em instancias

knn = KNeighborsClassifier(n_neighbors = 3) #Quantos vizinhos proximos ele vai usar para decidir a classe do exemplo novo
knn.fit(x_treinamento, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

#################################################################################

#Obtencao das previsoes

previsao = knn.predict(x_teste) #Usamos os dados das categorias do teste

print('PREVISAO: ', previsao)

################################################################################

#Agora vamos analisar a taxa de erros e acertos do modelo, atraves da matriz de confusao

confusao = confusion_matrix(y_teste, previsao)
print(confusao)

#Utilizamos tambem o accuracy para determinar a taxa de acerto
taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print(taxa_acerto)