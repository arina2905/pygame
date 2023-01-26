import pygame
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
screen = pygame.display.set_mode([1000, 600])

group_of_inyan = pygame.sprite.Group()
group_of_ini = pygame.sprite.Group()

dragon = Sprite(200, 400, 180, 'data/dragon.png')
inyan = Sprite(940, 240, 80, 'data/in_yan.png')
sky = Sprite(380, 0, 1200, 'fon_clouds.png')
ini = Sprite(1540, 240, 70, 'data/inyan.png')

group_of_inyan.add(inyan)
group_of_ini.add(ini)

sky.speed = [-5, 0]
inyan.speed = [-4, 0]
ini.speed = [-4, 0]

score = 0

font = pygame.font.Font(None, 50)

running = True
while running:
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

    if dragon.rect.x > 330:
        dragon.rect.x = 300

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                dragon.speed[1] = -200

    if pygame.sprite.spritecollide(dragon, group_of_inyan, False):
        score += 1
        print(score)

    if pygame.sprite.spritecollide(dragon, group_of_ini, False):
        running = False

    if dragon.rect.y < 300:
        dragon.speed = [15, 30]

    sky.update()
    dragon.update()
    inyan.update()
    ini.update()

    screen.fill([150, 200, 175])
    screen.blit(font.render(f'SCORE: {score}', True, (0, 0, 0), [150, 200, 175]), (50, 70))
    screen.blit(sky.image, sky.rect)
    screen.blit(dragon.image, dragon.rect)
    screen.blit(inyan.image, inyan.rect)
    screen.blit(ini.image, ini.rect)
    pygame.display.flip()
    pygame.time.delay(15)
pygame.quit()