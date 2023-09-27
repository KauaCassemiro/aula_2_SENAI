def Calculadora():  
    n1 = float(input("Digite um numero"))
    op = input("Digite a operação desejada")
    n2 = float(input("Digite um numero"))

    if op == "+":
        print(f'{n1} + {n2} = {n1 + n2}')
    if op == "x" or op == "*":
        print(f'{n1} x {n2} = {n1 * n2}')
    if op == "-":
        print(f'{n1} - n2 =  {n1 - n2}')
    if op == "/":
        print(f'{n1} / {n2} = {n1 / n2}')

Calculadora()