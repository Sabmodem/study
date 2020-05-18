import pygame
import random

class orange:

    image_bg = None
    win_width = 0
    win_height = 0
    win_size = None
    win = None

    imagesRight = []
    imagesLeft = []
    img_index = 0

    h_w = 0
    h_h = 0
    pos_x = 150  # начальная позиция X человека
    pos_y = 0  # начальная позиция Y человека
    step = 0

    bomb_count = 50  # количество бомбочек
    bomb_list = []  # список бобмочек - как спавн препятствий
    bomb_images = []

    press_time = 0  # время удержания клавиши нажатой
    int_pressed = 100  # интервал паузы, потом смещение человека в mlsek

    time_fall = 0  # текущее время задержки падения всех бомбочек
    int_fall = 10  # интервал до следующего сдвига mlsek

    clock = None
    key = None

    isRight = False

    def __init__(self):

        pygame.init()

        self.image_bg = pygame.image.load('./orange/bg1200.jpg')  # загружаем фон игры
        self.win_width, self.win_height = self.image_bg.get_rect().size  # узнаём размеры фона
        self.win_size = (self.win_width, self.win_height)  # запоминаем размеры
        self.win = pygame.display.set_mode(self.win_size)  # делаем окно по размерам фона
        self.win.blit(self.image_bg, (0, 0))  # рисуем фон на окне

        img_namesRight = ('./orange/0r.png','./orange/1r.png','./orange/2r.png','./orange/3r.png','./orange/4r.png')  # имена рисунков шагов человека
        # Спрайти с пометкой 'r' для шагов вправо, 'l' для шагов влево
        for name in img_namesRight:
            self.imagesRight.append(pygame.image.load(name).convert_alpha())

        img_namesLeft = ('./orange/0l.png','./orange/1l.png','./orange/2l.png','./orange/3l.png','./orange/4l.png')
        for name in img_namesLeft:
            self.imagesLeft.append(pygame.image.load(name).convert_alpha())

        bomb_names = ['./bombs/red.png','./bombs/green.png']  # имена рисунков бобмочек
        for item in bomb_names:  # добавляем сами рисункци в список
            color = ''
            if item[8] == 'r':
                color = 'red'
            else:
                color = 'green'
            self.bomb_images.append((pygame.image.load(item).convert_alpha(),color)) # В объект бомбы добавляется еще и цвет

        spavn_y = 0
        for _ in range(self.bomb_count):
            objBomb = random.choice(self.bomb_images)  # случайный рисунок бомбочки
            img = objBomb[0]
            color = True if objBomb[1] == 'green' else False # Если зеленая, color = True
            x = random.randint(40, self.win_width-40)  # случайный отступ по X
            spavn_y += int(1.0 * random.randint(0, self.win_height))
            y = 25 - spavn_y  # отступ по Y с накоплением от предыдущей бомбочки
            v = random.randint(1, 10)  # случайная скорость падения
            bomb = [img, x, y, v, True, color]  # для каждой бомбочки свои параметры
            self.bomb_list.append(bomb)  # добавляем бомбу в

        self.img_index = 0  # индекс текущего образа человека
        self.h_w, self.h_h = self.imagesRight[self.img_index].get_rect().size  # размеры рисунка человека
        self.step = self.h_w // 3  # размер шага человека
        self.pos_x = 150  # начальная позиция X человека
        self.pos_y = self.win_height - self.h_h - 135  # начальная позиция Y человека
        self.win.blit(self.imagesRight[self.img_index], (self.pos_x, self.pos_y))  # рисуем текущий образ человека

        self.clock = pygame.time.Clock()  # объект для фиксации промежутков времени

        pygame.display.update()  # обновляем окно

        self.loop()             # Вызываем основной цикл

    def printing(self):

        self.win.blit(self.image_bg, (0, 0))  # рисуем фон на окне
        if self.isRight == True:
            self.win.blit(self.imagesRight[self.img_index], (self.pos_x, self.pos_y))  # рисуем человека поверх фона
        else:
            self.win.blit(self.imagesLeft[self.img_index], (self.pos_x, self.pos_y))  # рисуем человека поверх фона

        for i in range(self.bomb_count):  # для всех бомб из списка
            if self.bomb_list[i][4]:  # если бомба ещё не достигла дна
                self.win.blit(self.bomb_list[i][0], (self.bomb_list[i][1], self.bomb_list[i][2]))  # рисуем бомбу
                if self.bomb_list[i][2] > self.win_height or (self.bomb_list[i][2] > (self.win_height-self.pos_y) and \
                (self.pos_x - self.h_w//2) < self.bomb_list[i][1] < (self.pos_x + self.h_w//2)):  # если бомба достигла дна
                    if self.bomb_list[i][5] == True: # Если бомба зеленая, отключаем ее
                        self.bomb_list[i][4] = False

        pygame.display.update()  # обновляем окно

    def updateTime(self):
        self.clock.tick()  # в каждой итерации фиксируем время
        self.press_time += self.clock.get_rawtime()  # накапливаем время удержания
        self.time_fall += self.clock.get_rawtime()  # накапливаем время паузы

        if self.press_time > self.int_pressed:  # если превысили интервал паузы
            self.press_time = 0  # сбрасываем для следующего цикла удержания
        if self.time_fall >= self.int_fall:  # если превысили интервал паузы
            self.time_fall = 0  # сбрасываем для следующего цикла паузы

    def getKeys(self):
        if self.press_time == 0:
            self.key = pygame.key.get_pressed()  # узнаём какая клавиша нажата


    def checkEvents(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # если нажали ВЫХОД
                pygame.quit()

    def trafficMan(self):
        if self.press_time == 0:
            if self.pos_x > self.h_w and self.key[pygame.K_LEFT]:
                self.pos_x -= self.step  # движение влево
                self.img_index = (self.img_index + 1) % len(self.imagesRight)
                self.isRight = False
            if self.pos_x + self.step < self.win_width - self.h_w and self.key[pygame.K_RIGHT]:
                self.pos_x += self.step  # движение вправо
                self.img_index = (self.img_index + 1) % len(self.imagesLeft)  # 0 1 2 -> 3 => 0 1 2
                self.isRight = True

    def trafficBombs(self):
        if self.time_fall == 0:  # сбрасываем для следующего цикла паузы
            for i in range(self.bomb_count):  # для всех бомб из списка
                if self.bomb_list[i][4]:  # если бомба ещё не достигла дна
                    self.bomb_list[i][2] += self.bomb_list[i][3]  # смещаем её на шаг

    def loop(self):             # Основной цикл программы
        while True:
            self.updateTime()
            self.getKeys()
            self.trafficBombs()
            self.trafficMan()
            self.checkEvents()
            self.printing()
