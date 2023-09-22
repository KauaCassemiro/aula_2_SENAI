#ex1
n = 10
while n >= 1:
    print(n)
    n -= 1
    if n == 0:
        print("Fogo")

#ex2
num = int(input("Digite um nmero"))
lista = range(1,num,2)
soma = sum(lista )
print(soma)

#ex3
n = 1
while n <= 10:
    print(n * 1)
    n += 1

#ex4
n = 99
while n >= 1:
    print(n)
    n -= 2

#Teste de random ex1
import random
aleatorio = random.randint(5,10)
print(aleatorio)

#e2
import random
x = random.randint(1,10)
y = random.randint(1,10)
z = random.randint(1,10)
print(x , y, z)

#ex3
import random
lista = random.randrange(10,30)
print(lista)
