from turtle import *

def main():
    lados = 5
    angulo = 360 / lados


    speed(5)
    shape('turtle')
    pensize(5)
    color('Blue')

    for i in range(lados):
        forward(100)
        right(angulo)

if __name__ == '__main__':
    main()