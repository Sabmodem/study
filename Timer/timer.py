from tkinter import *
import time

class timer:
    win = None                  # Окно
    results = []                # Список с замерами
    mode = None                 # Сюда пишем дескриптор запланированного запуска счетчика
    labels = []                 # Сюда добавляем текстовые поля
    Buttons = []                # Сюда добавляем кнопки
    start = 0                   # Время начала работы
    cont = False                # Если требуется продолжить с места остановки
    stop = 0                    # Время остановки. Используется для возобновления счета
    run = False                 # Индикатор работы секундомера

    def __init__(self):
        self.win = Tk()
        self.win.title('Секундомер')
        self.win.geometry('900x600') # Создаем окно
        self.win.resizable(0,0)      # Нельзя изменять размеры

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
        self.Buttons.append(Button(self.win,text = 'Текущий',width = 10,command = self.fixResults)) # Подписываем кнопки

        self.Buttons[0].place(x = 100,y = 50)
        self.Buttons[1].place(x = 300,y = 50)
        self.Buttons[2].place(x = 500,y = 50)
        self.Buttons[3].place(x = 700,y = 50) # Расставляем кнопки

        self.win.bind('<space>',(lambda event: self.timerStart())) # Привязываем кнопки к функциям
        self.win.bind('<Return>',(lambda event: self.timerNull()))
        self.win.bind('<Escape>',(lambda event: self.timerClear()))
        self.win.bind('<BackSpace>',(lambda event: self.fixResults()))

        self.win.mainloop()     # Запускаем обработку сообщений


    def updateTimer(self):      # Обновление общих данных
        '''
        Метод обновления строки с временем и поля для замеров.
        В окно влезает только 26 результатов. Этого должно хватить на все случаи жизни,
        Так что поле прокрутки не предусмотрено. Самый старый результат срезается.
        Если время старта == 0, то обнуляем поле
        '''
        if self.start != 0:
            self.labels[1].config(text = self.timerStr())
            if len(self.results) > 26:
                self.labels[2].config(text = '\n'.join(self.results[len(self.results)-26::]))
            else:
                self.labels[2].config(text = '\n'.join(self.results))
        elif self.start == 0:
            self.labels[1].config(text = '0:0:0:0')

    def fixResults(self):
        '''
        Метод обновления строк с замерами. Срабатывает только когда счетчик запущен.
        Добавляет в список замеров новую запись и обновляет текстовое поле
        '''
        if self.run == True:
            self.results.append(self.timerStr())
            self.labels[2].config(text = '\n'.join(self.results))

    def timerStr(self):
        '''
        Получаем время работы счетчика в секундах, преобразуем его в читаемый формат.
        self.start хранит значение времени на момент запуска скрипта(Не счетчика!).
        time.time() возвращает время на момент запуска счетчика.
        Вычитаем это значение из времени запуска скрипта и получаем время работы счетчика.
        '''
        if self.mode:
            seconds = int(time.time() - self.start)
            return  str(str(seconds//3600) + ':' + str((seconds//60)%60) + ':' + str(seconds%60) + ':' + str(int((time.time() - self.start)*1000))[-3::])

    def manualStop(self):
        '''
        Ручная остановка таймера. Запоминаем время остановки, потом используем его
        Чтобы не потерять текущее значение счетчика. Прицнип аналогичен методу выше
        '''
        self.cont = True
        self.TimerStop()
        self.fixResults()
        self.stop = time.time()

    def TimerStop(self):
        '''
        Метод остановки таймера. Останавливает счетчик и обновляет надпись на кнопке стопа
        '''
        if self.run == True:
            self.run = False
            self.win.after_cancel(self.mode)
            self.Buttons[0].config(text = 'Старт', command = self.timerStart)
            self.win.bind('<space>',(lambda event: self.timerStart()))

    def timerStart(self):
        '''
        Метод запуска счетчика. Срабатывает только если счетчик остановлен.
        При self.cont == True запускает счетчик с места остановки, использует
        Для этого значение времени остановки(self.stop)
        Обновляет надпись на кнопке старта
        '''
        if self.run == False:
            if self.cont == False:
                self.start = time.time()
            else:
                self.start += time.time() - self.stop
                self.cont = False

            self.Buttons[0].config(text = 'Стоп', command = self.manualStop)
            self.win.bind('<space>',(lambda event: self.manualStop()))

            self.run = True
            self.cycle()

    def cycle(self):            # Это сам цикл счетчика
        self.updateTimer()
        self.mode = self.win.after(1,self.cycle) # Планирует задачу на запуск самого себя

    def timerClear(self):
        '''
        Метод очистки таймера. Останавливает счетчик и обнуляет все значения.
        '''
        self.cont = False
        self.TimerStop()
        self.results = []
        self.start = 0
        self.updateTimer()
        self.labels[2].config(text = '')

    def timerNull(self):
        '''
        Метод обнуления таймера. Обнуляет только счетчик времени, останавливает таймер
        '''
        self.cont = False
        self.TimerStop()
        self.start = 0
        self.updateTimer()
