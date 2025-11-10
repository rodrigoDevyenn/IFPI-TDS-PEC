def somar(x, y):
    return x + y

def main():
    
    s = 0
    while True:
        num = int(input())
        if num != 0:
            s = somar(s, num)
        else:
            break
    
    print(s)

if __name__ == '__main__':
    main()