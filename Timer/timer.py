from tkinter import *

class timer:
    win = None
    timeInt = None
    results = []
    mode = None
    labels = []
    Buttons = []

    def __init__(self):
        self.win = Tk()
        self.win.title('Секундомер')
        self.win.geometry('900x600') # Создаем окно

        self.timeInt = [0,0,0,0] # Тут будем хранить счетчик времени

        self.labels.append(Label(self.win, text="Секундомер"))  # строка названия
        self.labels.append(Label(self.win,text = '0:0:0:0'))       # сюда будем выводить время
        self.labels.append(Label(self.win,text = ''))       # Замеры

        self.labels.append(Label(self.win,text = 'Space'))
        self.labels.append(Label(self.win,text = 'Enter'))
        self.labels.append(Label(self.win,text = 'Esc'))
        self.labels.append(Label(self.win,text = 'BackSpace')) # Подписи для кнопок


        self.labels[0].place(x = 400,y = 10)
        self.labels[1].place(x = 410,y = 120)
        self.labels[2].place(x = 410,y = 150)

        self.labels[3].place(x = 120, y = 90)
        self.labels[4].place(x = 320, y = 90)
        self.labels[5].place(x = 520, y = 90)
        self.labels[6].place(x = 720, y = 90) # Расставляем текстовые поля


        self.Buttons.append(Button(self.win,text = 'Старт',width = 10,command = self.timerStart))
        self.Buttons.append(Button(self.win,text = 'Обнулить',width = 10,command = self.timerNull))
        self.Buttons.append(Button(self.win,text = 'Очистить',width = 10,command = self.timerClear))
        self.Buttons.append(Button(self.win,text = 'Текущий',width = 10,command = self.timerCurrent))

        self.Buttons[0].place(x = 100,y = 50)
        self.Buttons[1].place(x = 300,y = 50)
        self.Buttons[2].place(x = 500,y = 50)
        self.Buttons[3].place(x = 700,y = 50) # Настраиваем кнопки

        self.win.bind('<space>',(lambda event: self.timerStart())) # Привязываем кнопки
        self.win.bind('<Return>',(lambda event: self.timerNull())) # К функциям
        self.win.bind('<Escape>',(lambda event: self.timerClear()))
        self.win.bind('<BackSpace>',(lambda event: self.timerCurrent()))

        self.win.mainloop()     # Запускаем обработку сообщений


    def updateTimer(self):      # Обновление общих данных
        self.labels[1].config(text = self.timerStr())
        if len(self.results) > 26:
            self.labels[2].config(text = '\n'.join(self.results[len(self.results)-26::]))
        else:
            self.labels[2].config(text = '\n'.join(self.results))

    def fixResults(self):       # Обновление строк с замерами
        self.results.append(self.timerStr())
        self.labels[2].config(text = '\n'.join(self.results))

    def timerStr(self):         # Получаем строку с временем
        return  str(str(self.timeInt[0]) + ':' + str(self.timeInt[1]) + ':' + str(self.timeInt[2]) + ':' + str(self.timeInt[3]))

    def manualStop(self):       # Остновка таймера кнопкой
        self.TimerStop()
        self.fixResults()
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))

    def TimerStop(self):        # Выходим из цикла счета времени
        self.win.after_cancel(self.mode)

    def timerStart(self):       # Запуск таймера
        self.Buttons[0].config(text = 'Стоп', command = self.manualStop)
        self.win.bind('<space>',(lambda event: self.manualStop()))

        self.timeInt[3] += 1    # Считаем время
        if self.timeInt[3] == 1000:
            self.timeInt[3] = 0
            self.timeInt[2] += 1
        if self.timeInt[2] == 60:
            self.timeInt[2] = 0
            self.timeInt[1] += 1
        if self.timeInt[1] == 60:
            self.timeInt[1] = 0
            self.timeInt[0] += 1

        self.updateTimer()
        self.mode = self.win.after(1,self.timerStart)

    def timerCurrent(self):     # Фиксируем замеры
        self.fixResults()

    def timerClear(self):       # Очистка таймера
        self.TimerStop()
        self.timeInt = [0,0,0,0]
        self.results = []
        self.fixResults()
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))

    def timerNull(self):        # Обнуление таймера
        self.TimerStop()
        self.timeInt = [0,0,0,0]
        self.updateTimer()
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))
