# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:48:11 2021

@author: ramon
"""

# Numpy - Modulo 8

import numpy as np

#Criando o array

lista1 = np.array([10,28,32,18,48])
print(lista1)


#Podemos determinar o tipo de array implicitamente e explicitamente
lista2 = np.array([1.7, 2.1, 3.1, 4.1, 5.1], dtype = np.float64)
print(lista2)

lista3 = np.array([1.7, 2.1, 3.1, 4.1, 5.1], dtype = np.int64)
print(lista3)

#Podemos tambem converter o tipo de um array

lista4 = np.array([1.6, 2.3, 5.4, 8.2])

lista5 = lista4.astype(np.int32)
print(lista5)

#Podemos usar o Numpy para fazer matrizes com varias dimensoes
lista6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(lista6)

#Podemos fazer arrays com valores aleatorios (determinamos o numero de linhas e colunas)
lista7 = np.empty([5,4], dtype = np.int32)
print(lista7)

#Podemos fazer arrays com valores de zero (determinamos o numero de linhas e colunas)
lista8 = np.zeros([5,4], dtype = np.int32)
print(lista8)

#Podemos fazer arrays com valores de 1 (determinamos o numero de linhas e colunas)
lista9 = np.ones([5,4], dtype = np.int32)
print(lista9)

#Podemos fazer arrays quadradas em que as diagonais sao compostas de 1 e o restante, 0 (determinamos o tamanho do quadrado ou retangulo)
lista10 = np.eye(5,5)
print(lista10)

#Cria 2 numeros aleatorios
aleatorio1 = np.random.random((2))
print(aleatorio1)

#Cria 2 numeros aleatorios podendo ser positivos ou negativos
aleatorio2 = np.random.randn((2))
print(aleatorio2)

#Crio uma matriz composta por numeros aleatorios (defino tambem o numero de linhas e colunas)
#Multiplico por 100 para mudar a escala dos numeros
aleatorio3 = (100*np.random.random((4,4)))
print(aleatorio3)

#Crio numeros aleatorios que eu posso acessar denovo quando eu rodar o codigo (gravo os numeros atraves de uma semente)
#Toda vez que eu rodar o codigo, terei 3 numeros exatamente iguais, porem, gerados aleatoriamente na semente

semente1 = np.random.default_rng(1) #1 para uma sequencia de numeros, 2 para outra sequencia, 3 para outra...
aleatorio4 = semente1.random(3) #quantidade de numeros aleatorios
print(aleatorio4)

semente1 = np.random.default_rng(1) #Nao mudo o valor da semente
aleatorio4 = semente1.random(3) #quantidade de numeros aleatorios
print(aleatorio4)

semente1 = np.random.default_rng(2) #Mudo o valor da semente
aleatorio4 = semente1.random(3) #quantidade de numeros aleatorios
print(aleatorio4)

#Posso gerar uma matriz de numeros inteiros aleatorios baseados na semente
aleatorio5 = semente1.integers(10, size = (4,4)) #aleatorios de 0 a 10
print(aleatorio5)

#Posso criar um array que remove os numeros repetidos
lista11 = np.array([1,2,3,4,5,1,3,11,14,2,2])
lista11 = np.unique(lista11)

print(lista11)

#Manipulando elementos do array
lista12 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(lista12)

print(lista12[1][1]) #Mostra um elemento especifico (primeiro retangulo = caixas, segundo retangulo = um dos 3 numeros da caixa)
print(lista12.shape) #Mostra o tamanho do vetor (linhas e colunas)

#Operacoes Matematicas
print(lista12.max()) #Mostra o maior valor presente na matriz
print(lista12.min()) #Mostra o minimo valor presente na matriz
print(lista12.sum()) #Soma todos os valores da matriz
print(lista12.mean()) #Media de todos os valores da matriz
print(lista12.std()) #Desvio padrao de todos os valores da matriz

#Funcoes Universais
lista13 = np.array([1,2,3,4,5])
print(lista13)

print(np.sqrt(lista13)) #Raiz quadrada de todos os elementos
print(np.exp(lista13)) #Valor do exponencial de todos os elementos

#Extrair elementos
lista14 = np.array([1,2,3,4,5,6,13,14,54,55])
print(lista14[0]) #Elemento simples
print(lista14[0:6]) #Exibe do elemento 0 ao 6
print(lista14[1:]) #Exibe todos os elementos depois do elemento 1
print(lista14[-3:]) #Mesma logica, porem, de tras para frente

#Extrair linhas e colunas
lista15 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(lista15)

lista15_linha1 = lista15[0,:] #Salva a linha 0 e todos os elementos presentes na linha
print('Linha 1:',lista15_linha1)

lista15_coluna1 = lista15[:, 0] #Salva a coluna 0 e todos os elementos presentes na coluna
print('Coluna 1:', lista15_coluna1)

#Adicao e Multiplicacao de Matrizes
print('__________________________________')
lista16 = np.array([[1,2], [3,4]])
lista17 = np.array([[5,6], [7,8]])

print(lista16)
print(lista17)

print('________________________________________')
adicao = lista16 + lista17
multiplicacao = lista16 * lista17

print(adicao)
print(multiplicacao)

#Criando uma matriz com 10 elementos em um arranjo especifico e mudando o arranjo
lista18 = np.arange(10).reshape((5,2))
print(lista18)

lista19 = lista18.T 
print(lista19) #Lista 19 se transformou na lista 18 na horizontal

#Logica de Matrizes
print('____________________________________________')
lista20 = np.random.randn(4,4) #Crio uma matriz aleatoria de 4 por 4
print(lista20)

logica1 = lista20 > 0 #Me retornara valores de True ou False para cada elemento da matriz
print(logica1)

logica2 = np.where(lista20 > 0, 1, 0) #Onde lista for maior que 0, coloque 1, caso contrario, coloque 0
print(logica2)



