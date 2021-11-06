from PIL import Image
import commands

class art:
    img = None
    name = None
    height = None
    width = None

    def __init__(self):
        try:
            print('Вас приветствует скрипт перевода картинок в символы, "ASCII ART"')
            self.change_img() #Вводим имя файла с клавиатуры
            self.listen() #Вызываем цикл обработки сообщений
        except Exception as exc:
            print(str(exc))


    def change_img(self):
        try:
            '''
            Записываем данные в атрибуты класса
            '''
            print('Введите имя файла с картинкой',  '\n\033[96m(ART)\033[0m',end = ' ')
            img_name = str(input())
            self.img = Image.open('./sources/' + img_name)
            self.name = img_name
            self.width, self.height = self.img.size
            print('Файл:', self.name + '.','Размерность:', str(self.width) + 'x' + str(self.height))
        except Exception as exc:
            print(str(exc))

    def save(self):
        '''
        Метод сохранения картинки в файл. Испольует средтва библиотеки PIL
        '''
        self.img.save('./sources/_' + self.name)
        print('Сохранено в', '_' + self.name)

    def show_help(self):
        '''
        Метод вывода списка команд
        '''
        print('\n'.join(commands.help))

    def resize_auto(self,height_new):
        '''
        Метод изменения размера с автоматическим подгоном длины под ширину
        '''
        try:
            self.width = self.width // (self.height//height_new)
            self.height = height_new
            self.img = self.img.resize((self.width, self.height), Image.ANTIALIAS)
            print('Размерность изменена:', str(self.width) + 'x' + str(self.height))
        except Exception as exc:
            print(exc)

    def resize(self,size):
        '''
        Метод изменения размера вручную
        '''
        try:
            self.width = size[0]
            self.height = size[1]
            self.img = self.img.resize((self.width, self.height), Image.ANTIALIAS)
            print('Размерность изменена:', str(self.width) + 'x' + str(self.height))
        except Exception as exc:
            print(exc)

    def invert_color(self):
        '''
        Метод инвертирования цвета картинки
        '''
        try:
            for y in range(self.height):
                for x in range(self.width):
                    r,g,b = self.img.getpixel((x,y))
                    self.img.putpixel((x,y),(255 - r, 255 - g, 255 - b))
            print('Цвет инвертирован')
        except Exception as Exc:
            print(exc)


    def invert_hor(self):
        '''
        Метод инвертирования картинки по горизонтали
        '''
        try:
            inverted = Image.new('RGB',(self.width,self.height)) #Создаем новое изображение(по умолчанию черного цвета) и перезаписываем его инвертированным
            for y in range(self.height):
                for x in range(self.width):
                    inverted.putpixel((self.width - (x + 1), y),self.img.getpixel((x,y)))
            self.img = inverted
            print('Инвертировано по горизонтали')
        except Exception as exc:
            print(exc)


    def invert_ver(self):
        '''
        Метод инвертирования изображения по вертикали. Аналогично методу выше
        '''
        try:
            inverted = Image.new('RGB',(self.width,self.height))
            for y in range(self.height):
                for x in range(self.width):
                    inverted.putpixel((x, self.height - (y + 1)),self.img.getpixel((x,y)))
            self.img = inverted
            print('Инвертировано по вертикали')
        except Exception as exc:
            print(exc)

    def show_dicts(self):
        '''
        Метод вывода словарей для конвертирования в символы(файла symbols.ini)
        '''
        infile = open('symbols.ini','r')
        print(''.join(infile.readlines()), end = '')

    def convert(self,n):
        '''
        Метод конвертирования картинки в символы
        '''
        try:
            infile = open('symbols.ini')
            outfile = open(str('./sources/' + self.name + '.txt'),'w') #Открываем выходной файл в ./sources/
            symbols = None
            for i in range(n):
                symbols = infile.readline()[3:-1] #Считываем нужный словарь по номеру, введенному пользователем
            count = len(symbols)
            full = 256 + 256 + 256  # максимальное значение
            segment = full // count  # длина сегмента
            result = ''
            for y in range(self.height):
                for x in range(self.width):
                    r, g, b = self.img.getpixel((x, y))
                    color = r + g + b
                    pos = (color // segment) - 1
                    result += symbols[pos] * 2
                result += '\n'
            outfile.write(result)
            infile.close()
            outfile.close() #Закрываем все файлы после записи конвертированной картинки
            print('Конвертировано в', self.name + '.txt')
        except Exception as exc:
            print(exc)

    def check_msg(self, msg):
        '''
        Метод обработки сообщений. Проверяет сообщение пользователя на наличие команд
        '''
        if msg[0] == commands.commands[0]:
            self.resize_auto(int(msg[1::]))
        elif msg[0] == commands.commands[1]:
            self.resize(tuple(map(int,msg[1::].split())))
        elif msg == commands.commands[2]:
            self.invert_color()
        elif msg == commands.commands[3]:
            self.invert_hor()
        elif msg == commands.commands[4]:
            self.invert_ver()
        elif msg[0] == commands.commands[5]:
            self.convert(int(msg[1::]))
        elif msg == commands.commands[6]:
            self.save()
        elif msg == commands.commands[7]:
            self.show_dicts()
        elif msg == commands.commands[8]:
            self.change_img()
        elif msg == commands.commands[10]:
            self.show_help()
        else:
            print('Некорректный ввод')

    def listen(self):
        '''
        Цикл обработки сообщений. Читает ввод пользователя и перенаправляет в метод обработки сообщений
        '''
        self.show_help() #Перед запуском покажем меню команд
        while True:
            try:
                print('\033[96m(ART)\033[0m', end = ' ') #Выводим строку приглашения
                msg = str(input())
                if msg == commands.commands[9]: #Проверяем, является ли сообщение сигналом к выходу
                    return 0
                else:
                    self.check_msg(msg)
            except Exception as exc:
                print(exc)
