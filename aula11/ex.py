#ex1
multiplicacao = lambda a,: a*2
print(multiplicacao(10))

#ex2
soma = lambda a,b: a+b
print(soma(10,20))

#ex3
numeros = [15,12,10,26,28,56,84]
pares = list(filter(lambda x : x % 2 == 0, numeros))

print(f'Os numeros {pares} dessa lista são parea')

#ex4
convert = lambda x: x.upper()
print(convert('hello'))

#ex5
multiplica = lambda a,b,c: a*b*c
print(multiplica(10,20,30))