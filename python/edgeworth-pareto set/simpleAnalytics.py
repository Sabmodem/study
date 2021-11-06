#!/usr/bin/python
from tkinter import *
from tkinter import messagebox

class simpleAnalytics:
    def __init__(self):
        self.win = Tk()
        self.win.title('Множество Эджворта-Парето')
        self.win.geometry('500x370') # Создаем окно

        self.criteriaRadioButtons = list()
        self.dataEntriesRows = list()
        self.dataRowCount = StringVar()
        self.criteriaCount = StringVar()

        self.criteria = list()
        self.criteriaText = list()

        self.data = list()
        self.outList = list()

        self.drow()
        self.win.mainloop()

    def drow(self):
        criteriaFrame = self.sendCriteriaFrame()
        dataFrame = self.sendDataFrame()
        computeButton = Button(self.win, text = 'Вычислить',width = 10, height = 1, command = self.compute).place(x = 200, y = 335)
        Label(self.win, text = 'Введите количество критериев:').place(x = 10, y = 15)
        Entry(self.win, textvariable = self.criteriaCount, bd = 3).place(x = 220, y = 10)
        Label(self.win, text = 'Введите количество полей ввода:').place(x = 10, y = 40)
        Entry(self.win, textvariable = self.dataRowCount, bd = 3).place(x = 220, y = 35)
        createInputWidgets = Button(self.win, text = 'Добавить\nполя ввода',width = 8, height = 3, command = lambda: self.createInputWidgets(criteriaFrame, dataFrame)).place(x = 400, y = 5)

    def sendCriteriaButtons(self, frame):
        for i in self.criteriaRadioButtons:
            i[0].destroy()
            i[1].destroy()
        self.criteriaRadioButtons = list()
        self.criteria = list()
        for i in range(int(self.criteriaCount.get())):
            criterion = BooleanVar()
            buttonMax = Radiobutton(frame, text = 'max', variable = criterion, value = 1)
            buttonMin = Radiobutton(frame, text = 'min', variable = criterion, value = 0)
            self.criteriaRadioButtons.append((buttonMax,buttonMin))
            self.criteriaRadioButtons[-1][0].place(x = 30 + (len(self.criteriaRadioButtons)-1) * 100, y = 10)
            self.criteriaRadioButtons[-1][1].place(x = 30 + (len(self.criteriaRadioButtons)-1) * 100, y = 45)
            self.criteria.append(criterion)

    def sendCriteriaFrame(self):
        criteriaScrollCanvas = Canvas(self.win,width = 470, height = 100, background = 'gray75')
        criteriaFrame = Frame(criteriaScrollCanvas, width = 2000, height = 2000, background = 'gray75')
        criteriaScrollCanvas.place(x = 10, y = 90)
        criteriaFrameScrollBar = Scrollbar(self.win, orient = 'horizontal', command = criteriaScrollCanvas.xview)
        criteriaFrameScrollBar.place(x = 10, y = 180)
        criteriaScrollCanvas.create_window(0, 0, anchor='nw', window=criteriaFrame)
        criteriaScrollCanvas.update_idletasks()
        criteriaScrollCanvas.configure(xscrollcommand=criteriaFrameScrollBar.set)
        return(criteriaFrame)

    def sendDataFrame(self):
        dataScrollCanvas = Canvas(self.win,width = 470, height = 105, background = 'gray75')
        dataScrollCanvas.place(x = 10, y = 220)
        dataFrame = Frame(dataScrollCanvas, width = 2000, height = 2000, background = 'gray75')
        dataFrameScrollBarX = Scrollbar(self.win, orient = 'horizontal', command = dataScrollCanvas.xview)
        dataFrameScrollBarY = Scrollbar(self.win, orient = 'vertical', command = dataScrollCanvas.yview)
        dataFrameScrollBarX.place(x = 10, y = 315)
        dataFrameScrollBarY.place(x = 470, y = 300)
        dataScrollCanvas.create_window(0, 0, anchor='nw', window=dataFrame)
        dataScrollCanvas.update_idletasks()
        dataScrollCanvas.configure(xscrollcommand=dataFrameScrollBarX.set)
        dataScrollCanvas.configure(yscrollcommand=dataFrameScrollBarY.set)
        return(dataFrame)

    def createInputWidgets(self, criteriaFrame, dataFrame):
        try:
            self.sendCriteriaButtons(criteriaFrame)
            self.sendEntriesRows(dataFrame)
            Label(self.win, text = 'Настройте критерии:').place(x = 10, y = 70)
            Label(self.win, text = 'Введите данные:').place(x = 10, y = 200)
        except(ValueError):
            messagebox.showerror('Ошибка', 'Должно быть введено число')
            return

    def sendEntriesRows(self, frame):
        for i in self.dataEntriesRows:
            for k in i:
                k.destroy()
        self.dataEntriesRows = list()
        for i in range(int(self.dataRowCount.get())):
            entryRow = list()
            for k in range(int(self.criteriaCount.get())):
                entry = Entry(frame, textvariable = StringVar(), bd = 3)
                entryRow.append(entry)
                entryRow[-1].place(x = 10 + k * 150, y = i * 25)
            self.dataEntriesRows.append(entryRow)

    def fillDataArray(self):
        try:
            for i in self.dataEntriesRows:
                row = list()
                for k in i:
                    row.append(int(k.get()))
                self.data.append(row)
                self.outList.append(row)
        except(ValueError):
            messagebox.showerror('Ошибка', 'Должно быть введено число')
            return


    def setCriteria(self):
        for i in self.criteria:
            if i.get() == 1:
                self.criteriaText.append('max')
            else:
                self.criteriaText.append('min')

    def removeItemFromOutputList(self,k):
        try:
            self.outList.remove(self.data[k])
        except ValueError:
            return True
        return False

    def compute(self):
        self.fillDataArray()
        self.setCriteria()
        for i in range(len(self.data)):
            for k in range(len(self.data)):
                for mainCriterion in range(len(self.criteriaText)):
                    condition = list()
                    for secondCriterion in range(len(self.criteriaText)):
                        if secondCriterion == mainCriterion:
                            if self.criteriaText[secondCriterion] == 'max':
                                condition.append(self.data[i][secondCriterion] > self.data[k][secondCriterion])
                            else:
                                condition.append(self.data[i][secondCriterion] < self.data[k][secondCriterion])
                        else:
                            if self.criteriaText[secondCriterion] == 'max':
                                condition.append(self.data[i][secondCriterion] >= self.data[k][secondCriterion])
                            else:
                                condition.append(self.data[i][secondCriterion] <= self.data[k][secondCriterion])
                                # print(visuals)
                    if all(condition):
                        if(self.removeItemFromOutputList(k)):
                            continue

        outStr = str()
        for i in self.outList:
            outRow = str()
            for k in i:
                outRow += str(k) + ' , '
            outStr += outRow[:-3] + '\n'
        messagebox.showinfo('done',outStr)
