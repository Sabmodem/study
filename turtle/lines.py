from turtle import *

class lines:
    x = None
    y = None
    colors = None #Контейнер с цветами
    color_cur = None #Текущий цвет линии

    def __init__(self,x,y,colors = None):
        penup()
        pensize(10)
        self.colors = colors
        if colors != None:
            self.color_cur = len(self.colors) - 1
        self.coords(x,y)

    def color_change(self): #Смена текущего цвета линии
        if self.color_cur < ((len(self.colors))-1):
            self.color_cur += 1
        else:
            self.color_cur  = 0
        return self.colors[self.color_cur]

    def lines_ver(self): #Вертикальные линии
        print('Введите количество линий')
        n = int(input())
        if self.colors != None:
            for _ in range(n):
                pendown()
                color(self.color_change())
                forward(500)
                penup()
                self.coords(self.x,self.y - 20)
            done()

    def lines_hor(self): #Горизонтальные линии
        print('Введите количество линий')
        n = int(input())
        right(90)
        for _ in range(n):
            pendown()
            forward(500)
            penup()
            self.coords(self.x + 20, self.y)
        done()

    def spiral(self): #Спираль
        print('Введите количество витков')
        n = int(input())
        tmp = 10
        pendown()
        for _ in range(n):
            forward(tmp)
            left(90)
            tmp += 10
        done()

    def coords(self,x,y): #Метод установки координат
        self.x = x
        self.y = y
        setx(self.x)
        sety(self.y)
