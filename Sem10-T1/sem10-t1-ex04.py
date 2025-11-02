def montarString(st, n):
    if n == 1000:
        st = st + str(n) + '.'
    else: 
        st = st + str(n) + ', '
    return st

def main():
    string = ''
    for i in range(10, 1001, 10):
        string = montarString(string, i)
    print(string)

if __name__ == '__main__':
    main()