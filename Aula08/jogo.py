import random
chance= 3
while chance <=3:
    aleatorio= random.randint(1,30)
    chute= int(input('digite um numero entre 1 a 30: '))

    if chute == aleatorio:
            print('voce acertouu')
            break
    else:
        chance -= 1
        print(f'errouu, o numero era {aleatorio}, você tem: {chance} chances')
        
    if chance == 0:
        print('Game over')
        break