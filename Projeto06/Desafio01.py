from random import *

def menu():
    return ('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

def main():

    print(menu())
    score = 0
    for attempt in range(3):
        print('\nEscolha uma porta (1, 2 ou 3):')
        portaEscolhida = input()
        portaEscolhida = int(portaEscolhida)

        portaCerta = randint(1,3)

        print(f'A porta escolhida foi a {portaEscolhida}.')
        print(f'A porta certa é a {portaCerta}.')

        if portaCerta == portaEscolhida:
            print('Parabéns!')
            score += 1
        else:
            print('Que peninha!')
    print(f'Seu Score foi {score}.') 
    
if __name__ == '__main__':
    main()