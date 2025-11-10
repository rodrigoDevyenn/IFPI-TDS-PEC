
def inverte(n):
    num_inv = ''
    for i in range(len(str(n)),0,-1):
        num_inv = num_inv + str(n)[i - 1]
    return int(num_inv)

def main():
    
    print('Vamos inverter um número!')
    num = int(input('Insira o número: '))
    print(f'O número invertido é {abs(inverte(num))}.')

if __name__ == '__main__':
    main()