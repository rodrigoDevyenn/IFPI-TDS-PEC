
def menor(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c

def medio(a, b, c):
    if (a >= b and a <= c) or (a >= c and a <= b):
        return a
    elif (b >= a and b <= c) or (b >= c and b <= a):
        return b
    elif (c >= a and c <= b) or (c >= b and c <= a):
        return c
    
def maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    
def main():

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    print(menor(num1, num2, num3))
    print(medio(num1, num2, num3))
    print(maior(num1, num2, num3))

if __name__ == '__main__':
    main()