# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:45:32 2021

@author: ramon
"""

#Tratamento de Dados - Modulo 10

import pandas as pd
import seaborn as srn #Graficos
import statistics as sts

#DataSet de um banco onde usa dados historicos de clientes que sairam ou nao da empresa

#Abrindo e lendo as informacoes do dataset
dataset = pd.read_csv('C:/Users/ramon/Desktop/CienciaDeDados/datasets/Churn.csv', sep=';') #Importante: use o sep


#Renomeando as colunas
dataset.columns = ['ID', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio', 'Saldo', 'Produtos', 'TemCartCredito',
                  'Ativo', 'Salario', 'Saiu']



#####################################################################################################################

#Analise Exploratoria de Dados Categoricos (divididos em categorias ao inves de quantidades) Presentes No DataSet

#Encontro todos os tipos de Estados presentes no dataset e quantas vezes cada um aparece
estados = dataset.groupby(['Estado']).size()
print(estados)

#Construo o grafico
#estados.plot.bar(color='green')

#####################################################################################################################

#Encontro todos os tipos de Generos presentes no dataset e quantas vezes cada um aparece
generos = dataset.groupby(['Genero']).size()
print(generos)

#Construo o grafico
#generos.plot.bar(color='green')

#####################################################################################################################

#Analise Exploratoria de Dados Numericos

#Score

print(dataset['Score'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo, 

#Construo o grafico boxplot
#srn.boxplot(dataset['Score']).set_title('Score')

#Construo o grafico em histograma
#srn.distplot(dataset['Score']).set_title('Score')

#####################################################################################################################
#Idade

#Nao posso ter idade negativa e nem com valores muito altos
print('___________________')
print(dataset['Idade'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo 

#Construo o grafico boxplot
#srn.boxplot(dataset['Idade']).set_title('Idade')

#Construo o grafico em histograma
#srn.distplot(dataset['Idade']).set_title('Idade')

#####################################################################################################################
#Saldo

#Algumas pessoas de fato podem ter saldo de zero na conta
print('___________________')
print(dataset['Saldo'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo, 

#Construo o grafico boxplot
#srn.boxplot(dataset['Saldo']).set_title('Saldo')

#Construo o grafico em histograma
#srn.distplot(dataset['Saldo']).set_title('Saldo')

#####################################################################################################################
#Salario

#Algumas pessoas de fato podem ter salario de zero
print('___________________')
print(dataset['Salario'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo, 

#Construo o grafico boxplot
#srn.boxplot(dataset['Salario']).set_title('Salario')

#Construo o grafico em histograma
#srn.distplot(dataset['Salario']).set_title('Salario')

#####################################################################################################################
#Corrigindo Valores Nulos
print('_________________________________________________________')
print('Corrigindo Valores Nulos')
print(dataset.isnull().sum()) #Onde ocorre valores nulos em toda a tabela

#Encontramos valores nulos em Genero e Salario. Primeiro, vamos tratar os dados quantitativos do Salario
#Vamos preencher o valor dos Salarios nulos com a mediana dos salarios

print(dataset['Salario'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo 

medianasalario = sts.median(dataset['Salario'])
print('Mediana do Salario: ', medianasalario)

#Vamos substituir os valores nulos de Salario pela mediana
dataset['Salario'].fillna(medianasalario, inplace=True) #Lembrando que inplace corresponde a gravar o dado na tabela de fato

#Vamos ver se conseguimos retirar os valores nulos
print(dataset['Salario'].isnull().sum()) #Temos 0 valores nulos agora

#####################################################################################################################
#Corrigindo Generos escritos de varias formas

print('_________________________________________________________')
print('Corrigindo Generos escritos de varias formas')

generos = dataset.groupby(['Genero']).size()
print(generos) #Temos F,Fem e Feminino para o genero Feminino e M e Masculino para o genero Masculino (devemos padronizar)

#Alem disso, precisamos retirar os generos preenchidos como nulo
print('Valores Nulos: ', dataset['Genero'].isnull().sum()) #Temos 8 valores nulos

#Vamos preencher os valores nulos como sendo Masculino, pois eles sao mais frequentes (representam a moda)
dataset['Genero'].fillna('Masculino', inplace=True)

#Agora que ja tratamos os valores nulos, vamos tratar a repeticao de generos

#Masculino
dataset.loc[dataset['Genero'] == 'M', 'Genero'] = 'Masculino'

print(dataset['Genero'].isnull().sum())
generos = dataset.groupby(['Genero']).size()
print(generos)

#Feminino
#dataset.loc[dataset['Genero'] == 'F', 'Genero'] = 'Feminino'
#dataset.loc[dataset['Genero'] == 'Fem', 'Genero'] = 'Feminino'
dataset.loc[dataset['Genero'].isin(['F','Fem']), 'Genero'] = 'Feminino'

print('___________________________________________')
print('Tratamento Final: ')

print(dataset['Genero'].isnull().sum())
generos = dataset.groupby(['Genero']).size()
print(generos) #Agora, Masculino e Feminino estao representados na tabela apenas pela palavra Masculino e Feminino

###################################################################################################

#Filtro a tabela em idade entre 18 a 55 anos e genero feminino

print('_____________________________________________________________')
print('Filtrar idades e Generos')

idades = dataset.loc[dataset['Idade'] > 18].loc[dataset['Idade'] < 55].loc[dataset['Genero'] == 'Feminino']
idadesfiltradas = idades.groupby(['Idade']).size()

print(idadesfiltradas)
#idadesfiltradas.plot.bar(color='green')

###################################################################################################

#Tratamento dos valores de Idade

print('_____________________________________________________________')
print('Tratamento dos valores de Idade')

print(dataset['Idade'].describe()) #Valores de Media, Mediana, Valor Minimo e Maximo 

medianaidade = sts.median(dataset['Idade'])
print('Mediana da Idade: ', medianaidade)

#Vamos substituir os valores nulos de Idade pela mediana
dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120)] = medianaidade 

print(dataset.groupby(['Idade']).size()) #Eliminamos dados com idades incompativeis com a realidade
#dataset['Idade'].plot.bar(color='green') => Esse grafico e bom em colunas categoricas 

#srn.distplot(dataset['Idade']).set_title('Idade') #Construimos um grafico de histograma


####################################################################################################

#Tratamento de dados duplicados usando a ID como referencia

print('_____________________________________________________________')
print('Dados duplicados')

print(dataset[dataset.duplicated(['ID'], keep=False)]) #Conferimos se existem dados duplicados na ID

#Vamos remover o elementos duplicados
dataset.drop_duplicates(subset = 'ID', keep='first', inplace=True) #Mantenho o primeiro elemento dos duplicados

#Conferimos se existem mais duplicados
print(dataset[dataset.duplicated(['ID'], keep=False)])

####################################################################################################

#Tratamento de Estados fora da regiao Sul

print('_____________________________________________________________')
print('Tratando Estados Fora da regiao Sul')

print(dataset.groupby(['Estado']).size())

#Vamos substituir os estados SP, RP e TD pela Moda (RS)

dataset.loc[(dataset['Estado']).isin(['SP', 'RP', 'TD']), 'Estado'] = 'RS'

print(dataset.groupby(['Estado']).size())

####################################################################################################

#Tratando salarios muito acima do desvio padrao

print('_____________________________________________________________')
print('Salarios muito acima do Desvio Padrao')


print(dataset.groupby(['Salario']).size())

desviopadrao = sts.stdev(dataset['Salario'])
print('Desvio Padrao dos Salarios: ', desviopadrao)

#Vamos checar para ver se existem salarios maiores que duas vezes o desvio padrao

print(dataset.loc[dataset['Salario'] >= 2* desviopadrao])

medianasalario = sts.median(dataset['Salario'])

#substituimos os valores maiores pela mediana
dataset.loc[dataset['Salario'] >= 2* desviopadrao, 'Salario'] = medianasalario

print(dataset.loc[dataset['Salario'] >= 2* desviopadrao])

#Criamos um grafico
#srn.distplot(dataset['Salario']).set_title('Salario')


####################################################################################################

#Finalizando o Tratamento

print('_____________________________________________________________')
print('Finalizando o Tratamento')

print(dataset.head())
print('Numero de Linhas e Colunas: ', dataset.shape)



 




