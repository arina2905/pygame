import pygame
from game import start_screen
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN

from the_end import my_animation
import sys
import os

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = [0, 0]

    def update(self):
        #изменения координат
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]


pygame.init()
size = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 50
startscreen = start_screen()
screen = pygame.display.set_mode([1000, 600])

group_of_inyan = pygame.sprite.Group()
group_of_ini = pygame.sprite.Group()

dragon = Sprite(200, 400, 180, 'data/dragon.png')
inyan = Sprite(940, 200, 80, 'data/in_yan.png')
sky = Sprite(380, 0, 1200, 'fon_clouds.png')
ini = Sprite(1540, 200, 115, 'data/inyan.png')

#группы спрайтов
group_of_inyan.add(inyan)
group_of_ini.add(ini)

#скорость
sky.speed = [-5, 0]
inyan.speed = [-4, 0]
ini.speed = [-4, 0]

#счет
score = 0

#level
level = 1

#для ускорения
next_boost = 13

font = pygame.font.Font(None, 50)

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



def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


'''def terminate():
        pygame.quit()
        sys.exit()'''

def ending():
        intro_text = [f'{score}',
                      'Поздравляю!!!']

        fon = pygame.transform.scale(load_image('zastavka.png'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, [0, 0 , 0])
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)


running = True
while running:
    #возвращение спрайта в начало для смена картинки (?)
    if sky.rect.x < -1000:
        sky.rect.x = 1000

    if ini.rect.x < -80:
        ini.rect.x = 1400

    if inyan.rect.x < -80:
        inyan.rect.x = 1400

    if dragon.rect.y > 30:
        dragon.speed = [0, 0]
    else:
        dragon.speed[1] += 1

    if dragon.rect.x > 180:
        dragon.rect.x = 180

    if score >= next_boost:
        inyan.speed[0] -= 2
        ini.speed[0] -= 3
        next_boost += 5

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            #ending()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                dragon.speed[1] = -200

    #проверки на столкновения спрайтов
    if pygame.sprite.spritecollide(dragon, group_of_inyan, False):
        score += 1
        print(score)

    if next_boost == 18:
        print(f', {next_boost}')
        level = 2
    if next_boost == 43:
        print(f', {next_boost}')
        level = 3
        #next_boost += 5

    if pygame.sprite.spritecollide(dragon, group_of_ini, False):
        running = False
        ending()
        print('loser')
    #возвращения дракона на исходное
    if dragon.rect.y < 300:
        dragon.speed = [15, 30]

    sky.update()
    dragon.update()
    inyan.update()
    ini.update()

    screen.fill([150, 200, 175])
    screen.blit(font.render(f'SCORE: {score}', True, (0, 0, 0), [150, 200, 175]), (50, 70))
    screen.blit(font.render(f'LEVEL: {level}', True, (0, 0, 0), [150, 200, 175]), (800, 70))
    screen.blit(sky.image, sky.rect)
    screen.blit(dragon.image, dragon.rect)
    screen.blit(inyan.image, inyan.rect)
    screen.blit(ini.image, ini.rect)
    #screen.blit(my_animation(12, 4, 48, 30, "image", (50, 50)))
    pygame.display.flip()
    pygame.time.delay(15)
pygame.quit()
