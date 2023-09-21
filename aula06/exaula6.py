#ex1
numeros = [1,2,3,4,5]
print(numeros)

#ex2
print(numeros[2])

#ex3
numeros.append(6)
print(numeros)

#ex4
numeros.remove(3)
print(numeros)

#ex5
frutas = ["Maça", "Morango", "Goiaba"]
concatenarLista = numeros + frutas
print(concatenarLista)

#ex6
for i in frutas:
    print(i)

#ex7
if 5 in numeros:
    print("Esse item já está na lista")
else:
    print("O item foi adicionado a lista")
