#funções 
def soma(): #def é pra definir como função
    a = 15
    b = 10
    print(a + b)
#isso é para chamar a função
#se não chamar ela não funciona
soma()

def cumprimento():
    n = input('digite seu nome')
    y = input('Digite sua idade')
    print(f'o nome do usuario é {n} e sua idade é {y}')

def sub():
    a = int(input('Digite um numero'))
    b = int(input('digite outro'))
    print(f'o resultado da subtração é: {a-b}')

cumprimento()
sub()