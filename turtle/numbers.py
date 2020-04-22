from turtle import *

class numbers:
    x = None
    y = None
    angle = None #Угол отколения от начального направления

    def __init__(self,x,y,number):
        penup()
        self.angle = 0
        pensize(10)
        self.coords(x,y) #Метод установки координат
        self.drow(str(number))

    def coords(self,x,y):
        self.x = x
        self.y = y
        setx(self.x)
        sety(self.y)
        if self.angle < 0: #Если есть отколения от начального направления, корректируем угол
            left(abs(self.angle))
            self.angle = 0
        else:
            right(self.angle)


    def zero(self):
        pendown()

        left(180)
        forward(100)
        left(90)
        forward(200)
        left(90)
        forward(100)
        left(90)
        forward(200)
        right(90)

        penup()
        self.coords(self.x + 150,self.y)

    def one(self):
        pendown()

        right(135)
        forward(141)
        left(180)
        forward(141)
        right(135)
        forward(200)

        penup()
        self.angle -= 90
        self.coords(self.x + 150,self.y)

    def two(self):
        pendown()

        left(180)
        forward(100)
        left(180)
        forward(100)
        right(90)
        forward(100)
        right(45)
        forward(141)
        left(135)
        forward(100)

        penup()
        self.coords(self.x + 150,self.y)

    def three(self):
        pendown()

        left(180)
        forward(100)
        left(180)
        forward(100)
        right(135)
        forward(141)
        left(135)
        forward(100)
        right(135)
        forward(141)
        penup()
        self.angle -= 135
        self.coords(self.x + 150,self.y)

    def four(self):
        pendown()
        right(90)
        forward(200)
        left(180)
        forward(100)
        left(90)
        forward(100)
        right(90)
        forward(100)
        penup()
        self.angle -= 270
        self.coords(self.x + 150,self.y)

    def five(self):
        pendown()

        right(180)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)

        penup()
        self.angle -= 180
        self.coords(self.x + 150,self.y)

    def six(self):
        pendown()

        right(135)
        forward(141)
        left(135)
        forward(100)
        for _ in range(3):
            right(90)
            forward(100)

        penup()
        self.angle -= 270
        self.coords(self.x + 150,self.y)

    def seven(self):
        pendown()

        left(180)
        forward(100)
        left(180)
        forward(100)
        right(135)
        forward(141)
        left(45)
        forward(100)


        penup()
        self.angle -= 90
        self.coords(self.x + 150,self.y)

    def eight(self):
        pendown()

        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(180)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(200)

        penup()
        self.angle -= 270
        self.coords(self.x + 150,self.y)

    def nine(self):
        pendown()

        for _ in range(4):
            right(90)
            forward(100)

        penup()
        right(90)
        forward(100)
        pendown()
        right(45)
        forward(141)

        penup()
        self.angle -= 135
        self.coords(self.x + 150,self.y)

    def check_msg(self,number): #Обработка сообщений
        if number == '0':
            self.zero()
        elif number == '1':
            self.one()
        elif number == '2':
            self.two()
        elif number == '3':
            self.three()
        elif number == '4':
            self.four()
        elif number == '5':
            self.five()
        elif number == '6':
            self.six()
        elif number == '7':
            self.seven()
        elif number == '8':
            self.eight()
        elif number == '9':
            self.nine()
        else:
            print('Некорректный ввод')

    def drow(self,number): #Цикл обработки сообщений
        for i in number:
            self.check_msg(i)
        done()
