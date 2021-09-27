#Listas - Pratica Python - Modulo 7

#Criando e Printando Listas:

lista1 = [1,2,3,4,5]
lista2 = ['1',2,'3',4.5,8.2, True]
lista3 = ['elemento1', 2, 3, lista1, 'ramon', [1,2,3,4], 4.7]
lista4 = list(range(0, 1))
lista5 = [1,2,3, list(range(4, 11))]

print (lista1)
print (lista2)
print (lista3)
print (lista4)
print (lista5)

#Contando numero de elementos de uma lista (posso fazer de duas formas):

print (len(lista3))

numerodeelementos = len(lista3)
print (numerodeelementos)

#Acessando elementos de uma lista (lembrando que a lista comeca no elemento 0)

print (lista3[0])
print (lista5[3])

#Alterando elementos de uma lista

lista1[0] = 'A'
print (lista1)

lista1[0] = 100
print (lista1)

#Percorrer uma lista
for n in range(0, len(lista1)):
    print (lista1[n])