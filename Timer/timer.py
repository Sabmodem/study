from tkinter import *
import time

class timer:
    win = None
    results = []
    mode = None
    labels = []
    Buttons = []
    start = time.time()
    cont = False                # Индикатор ручной остановки таймера
    stop = 0                    # Время остановки. Используется для возобновления счета

    def __init__(self):
        self.win = Tk()
        self.win.title('Секундомер')
        self.win.geometry('900x600') # Создаем окно

        self.labels.append(Label(self.win, text="Секундомер"))  # строка названия
        self.labels.append(Label(self.win,text = ''))       # сюда будем выводить время
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
        seconds = int(time.time() - self.start)
        return  str(str(seconds//3600) + ':' + str((seconds//60)%60) + ':' + str(seconds%60) + ':' + str(int((time.time() - self.start)*1000))[-3::])

    def manualStop(self):       # Остновка таймера кнопкой
        self.cont = True
        self.stop = time.time()
        self.TimerStop()
        self.fixResults()
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))

    def TimerStop(self):        # Выходим из цикла счета времени
        self.win.after_cancel(self.mode)

    def timerStart(self):       # Запуск таймера
        if self.cont == False:
            self.start = time.time()
        else:
            self.start += time.time() - self.stop
        self.Buttons[0].config(text = 'Стоп', command = self.manualStop)
        self.win.bind('<space>',(lambda event: self.manualStop()))
        self.cycle()

    def cycle(self):
        self.updateTimer()
        self.mode = self.win.after(1,self.cycle)

    def timerCurrent(self):     # Фиксируем замеры
        self.fixResults()

    def timerClear(self):       # Очистка таймера
        self.TimerStop()
        self.start = time.time()
        self.updateTimer()
        self.results = []
        self.fixResults()
        self.start = 0
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))

    def timerNull(self):        # Обнуление таймера
        self.TimerStop()
        self.start = time.time()
        self.updateTimer()
        self.start = 0
        self.Buttons[0].config(text = 'Старт', command = self.timerStart)
        self.win.bind('<space>',(lambda event: self.timerStart()))
