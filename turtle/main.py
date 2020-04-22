from turtle import *
import lines
import numbers

print(
    '1 : Начертить горизонтальные линии\n',
    '2 : Начертить цветные вертикальные линии\n',
    '3 : Начертить спираль\n',
    '4 : Начертить цифру\n',
    '5 : Начертить 6 цифр'
     )

n = int(input())

if n == 1:
    lines.lines(-300,300).lines_hor()
elif n == 2:
    lines.lines(-300,300,('red','green','blue')).lines_ver()
elif n == 3:
    lines.lines(0,0).spiral()
elif n == 4:
    numbers.numbers(0,0)
elif n == 5:
    numbers.numbers(-400,0)
