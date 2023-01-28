import sys
from email.mime import image

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


# pygame.constants необходим для создания условия выхода из цикла

def my_animation(w1, h1, k, fps, name, position):
    # список для хранения кадров и таймер
    animation_frames = []
    timer = pygame.time.Clock()

    # создаем экран и загружаем изображение в переменную sprite, установив методом convert_alpha необходимую прозрачность
    #scr = pygame.display.set_mode((160, 200), 0, 32)
    sprite = pygame.image.load("data/chel.png".format(name)).convert_alpha()

    # находим длину, ширину изображения и размеры каждого кадра
    width, height = sprite.get_size()
    w, h = width / w1, height / h1

    # счетчик положения кадра на изображении
    row = 0

    # итерация по строкам
    for j in range(int(height / h)):
        # производим итерацию по элементам строки
        for i in range(int(width / w)):
            # добавляем  в список отдельные кадры
            animation_frames.append(sprite.subsurface(pygame.Rect(i * w, row, w, h)))
        # смещаемся на высоту кадра, т.е. переходим на другую строку
        row += int(h)

    # счетчик
    counter = 0

    while True:
        # условие выхода из цикла - нажатие клавиши ESCAPE
        for evt in pygame.event.get():
            if evt.type == QUIT or (evt.type == KEYDOWN and evt.key == K_ESCAPE):
                sys.exit()
        # заполняем игровое поле красным цветом и методом blit вырисовываем на поверхности

        #scr.fill((150, 200, 175))
        #scr.blit(animation_frames[counter], position)

        # счетчик используемый как индекс в списке увеличивается до того как не превысит

        counter = (counter + 1) % k

        # обновляем экран
        pygame.display.update()
        timer.tick(fps)


if __name__ == "__main__":
    x = 30
    my_animation(12, 4, 48, x, "image", (50, 50))