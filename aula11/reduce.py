import reduce

# n = [ 100,200,300]
# soma = reduce(lambda x,y: x+y, n)
# print(soma)

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)