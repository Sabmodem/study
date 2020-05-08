r = 50  # сторона блока в пискелях
cnt_w = 9  # ширина стакана в блоках
cnt_h = 16  # высота стакана
sc_width = r * cnt_w  # ширина экрана в пикселях
sc_height = r * cnt_h  # высота экрана
sc_size = (sc_width, sc_height)  #
color_bg = (0, 55, 99)  # цвет фона
color_fg = (225, 125, 0)  # цвет контура

colors = [(225, 125, 0), (0, 225, 125), (0, 125, 225)]  # цвета блоков
index_color = 0  # начальный цвет

pos_x = cnt_w // 2
pos_y = 1

fall_time = 0
interval = 300  # mlsek
press_time = 0
int_pressed = 100  # mlsek
