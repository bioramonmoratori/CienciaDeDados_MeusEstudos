# Dicionarios, Sets e Tuplas - Modulo 8

#__________________Dicionario______________________

valor1 = ['casa','carro']

#Faco uma lista com chaves e valores respectivos
dicionario1 = {'Chave1':valor1, 'Chave2':8.2}

print (dicionario1['Chave1']) 

#Posso imprimir somente as chaves e somente os valores
chaves = dicionario1.keys()
valores = dicionario1.values()

print(chaves)
print(valores)

#Posso conferir se uma determinada chave esta contida no dicionario
print('Chave1' in dicionario1)
print('Chave2' in dicionario1)

#Posso conferir se um determinado valor esta contido nos valores do dicionario (tambem vale para as chaves)
print(valor1 in dicionario1.values())

#Deleta uma chave (so e permitido com chaves)
del dicionario1['Chave1']

print(dicionario1)

#Incluir uma chave
dicionario1['Chave3'] = 35

print(dicionario1)

#Tenta buscar uma chave
print(dicionario1.get('Chave3', 'Nao Encontrei Nenhuma Chave Com Esse Nome'))
print('>>>>>>>')
chavees = []
chavees = dicionario1.keys()
print(chavees[0])

#__________________Sets______________________

#Sets sao elementos que nao se repetem dentro de uma lista

set1 = {'Elemento1', 'Elemento2', 'Elemento3'}
print(set1)
print(len(set1))

set1.add('Elemento4')
print(set1)
print(len(set1))

#Se eu tentar adicionar um elemento que ja existe, ele nao adiciona nada
set1.add('Elemento4')
print(set1)

#__________________Tuplas______________________

#Tuplas sao listas de elementos que nao podem ser alterados

tupla1 = (1,2,3,4,5)

#Posso por uma tupla dentro de uma lista ou dicionario

dicionario2 = {(1,2):'Casa'}
print(dicionario2) 
