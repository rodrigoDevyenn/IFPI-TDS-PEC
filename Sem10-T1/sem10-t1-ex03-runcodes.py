
def media(s):
    return s / 100

def main():
    soma = 0 
    for i in range(100):
        num = int(input())
        soma = soma + num
    print(f'{media(soma):.2f}')
    

if __name__ == '__main__':
    main()
        