from turtle import *

def main():
    speed(11)
    shape('turtle')

    for count in range(30):
        forward(5)
        penup()
        forward(5)
        pendown()

if __name__ == '__main__':
    main()