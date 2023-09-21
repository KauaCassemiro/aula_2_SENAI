#gera um numero aleatorio 0. alguma coisa
import random

aleatorio = random.random()
print(aleatorio)

#numero aleatorio dentro de parametros ditos pelo programador
x = random.randint(1,10)
print(x)


#teste de joguinho
ale = int(input("Digite um numero"))
num_ale = random.randint(1,10)
if ale == num_ale:
    print("Você acertou, o numero é:" , num_ale)
else:
    print("Você errou, o numero é:" , num_ale)