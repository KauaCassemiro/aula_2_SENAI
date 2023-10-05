#elevar a 3 os numeros da lista

lista = [1,2,3,5]
quadrado = list(map(lambda x: x**3, lista)) 
print(quadrado)

#map mapeia todos os itens da lista
#lambda executa funções sem precisar declarar uma variavel

multiplicacao = lambda a,b: a*b
print(multiplicacao(10,20))
