#adc item na lista
lista = [1,5,6,4,"casa",9]
lista.append(48)
print(lista)

#remover item da lista pelo valor 
lista2 = [1,7,6,948,358]
lista2.remove(7)
print(lista2)

#remover item da lista pelo indice
lista3 = [5,6,158,325,12,987]
del lista3[3]

#mostra quantos elementos tem na lista
quant = len(lista3)
print(quant)

#acessa a lista e faz cada item ficar em uma linha só
lista4= [1,2,5,6,54,301,5205,777]
for i in lista4:
    print(i)