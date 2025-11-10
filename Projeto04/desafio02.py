from turtle import *

def main():
    speed(3)
    shape('turtle')

    for count in range(5):
        forward(50)
        right(72)
    
    penup()
    forward(100)
    pendown()

    for count in range(6):
        forward(50)
        right(60)

    penup()
    backward(300)
    pendown()

    for count in range(360):
        forward(1)
        right(1)



        

if __name__ == '__main__':
    main()