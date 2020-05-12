import pygame
from init import *

class tetris:
    index_color = index_color  # начальный цвет

    pos_x = pos_x
    pos_y = pos_y

    filled = []                     # Сюда пишем координаты залитых блоков
    pause = False                   # Переменная для реализации паузы
    active = True                   # Переменная для остановки игры

    win = None                  # Окно игры
    key = None                  # Сюда пишем нажатые клавиши

    press_time = press_time
    fall_time = fall_time
    clock = None


    def __init__(self):
        pygame.init()
        pygame.display.set_caption('tetRIS')
        self.win = pygame.display.set_mode(sc_size)
        self.win.fill(color_bg)
        pygame.draw.rect(self.win, colors[self.index_color], (self.pos_x*r, self.pos_y*r, r, r), 3)
        self.update()
        self.clock = pygame.time.Clock()

        self.cycle()

    def clock_update(self):     # Метод обновления счетчика времени
        self.clock.tick()
        self.fall_time += self.clock.get_rawtime()
        self.press_time += self.clock.get_rawtime()

    def check_events(self):     # Проверка сигналов к выходу и паузе
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
                self.pause = not self.pause

    def check_presses(self):    # Проверка нажатия клавиш
        if self.press_time >= int_pressed:
            self.press_time = 0
            if self.pos_y < cnt_h - 1:  # на дне стакана нельзя двигать блок
                if self.pos_x > 0 and self.key[pygame.K_LEFT]:
                    pygame.draw.rect(self.win, color_bg, (self.pos_x * r, self.pos_y * r, r, r), 3)
                    self.pos_x -= 1
                if self.pos_x < cnt_w - 1 and self.key[pygame.K_RIGHT]:
                    pygame.draw.rect(self.win, color_bg, (self.pos_x * r, self.pos_y * r, r, r), 3)
                    self.pos_x += 1
                if self.pos_x < cnt_w - 1 and self.key[pygame.K_DOWN]:
                    if (cnt_h - 1, self.pos_x) not in self.filled:
                        #Если на этой координате еще нет залитых блоков, то ставим блок в самый низ
                        pygame.draw.rect(self.win, color_bg, (self.pos_x * r, self.pos_y * r, r, r), 3)
                        self.pos_y = cnt_h - 1
                    else:
                        #Иначе гоним циклом координату пока не наткнемся на залитый блок. Ставим блок перед ним
                        pygame.draw.rect(self.win, color_bg, (self.pos_x * r, self.pos_y * r, r, r), 3)
                        while (self.pos_y,self.pos_x) not in self.filled:
                            self.pos_y += 1
                        self.pos_y -= 1


    def traffic(self):          # Тут двигаем блоки вниз
        if self.fall_time >= interval:
            self.fall_time = 0
            if self.pos_y < cnt_h - 1 and (self.pos_y+1,self.pos_x) not in self.filled:
                pygame.draw.rect(self.win, color_bg, (self.pos_x * r, self.pos_y * r, r, r), 3)
                self.pos_y += 1
            else:
                # Если текущая координата это дно или блок, подлежащий заполнению, добавляем его в список залитых
                pygame.draw.rect(self.win, colors[self.index_color], (self.pos_x * r, self.pos_y * r, r, r))  # заливка квадрата
                self.filled.append((self.pos_y,self.pos_x))
                #Если стакан полный, заканчиваем игру
                if self.pos_y == 1:
                    self.active = False
                    print('Стакан заполнен. Игра окончена')
                self.pos_y = 1
                self.pos_x = cnt_w // 2
                self.index_color = (self.index_color + 1) % len(colors)

        if self.pos_y < cnt_h - 1:
            pygame.draw.rect(self.win, colors[self.index_color], (self.pos_x * r, self.pos_y * r, r, r), 3)  # контур квадрата

    def update(self):           # Обновление окна игры
        pygame.display.update()

    def get_keys(self):
        self.key = pygame.key.get_pressed()  # Получаем список нажатых клавиш

    def cycle(self):            # Основной цикл, тут вызываем все методы и проверяем наполненность стакана
        while True:
            self.get_keys()
            self.clock_update()
            self.check_events()
            # self.check_pause()
            if self.pause == False:
                self.check_presses()
                self.traffic()
            self.update()
            if self.active == False:
                break
