import pygame
from scripts.level import Level
from scripts.slime import Entity
from scripts.player import Player
from scripts.config import *
import math
import random
import time

# init
pygame.init()
screenWidth = 900
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.SCALED + pygame.RESIZABLE)
clock = pygame.time.Clock()
startTicks = pygame.time.get_ticks()
pygame.display.set_caption('RPG Game')
fps = 60


enemyList = pygame.sprite.Group()
gameSprites = pygame.sprite.LayeredUpdates()

currentLevel = 0
nextLevel = False


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.scroll = [0, 0]

    def render(self, player):
        # scrolling camera
        self.scroll[0] += ((player.rect.x - self.scroll[0] - (screenWidth / 2)) + 10) / 20
        self.scroll[1] += (player.rect.y - self.scroll[1] - (screenHeight / 2)) / 20

        for sprite in gameSprites.sprites():
            sprite.image.set_colorkey((0, 0, 0))
            screen.blit(sprite.image, (sprite.rect.x - self.scroll[0], sprite.rect.y - self.scroll[1]))


def game():
    global nextLevel, currentLevel
    running = True
    # creating objects
    cam_group = CameraGroup()
    level = Level(gameSprites)
    level.loadMap()
    level.render()
    player = Player((level.levels[currentLevel].get('playerPosX'), level.levels[currentLevel].get('playerPosY')), gameSprites)
    last_time = time.time()
    # slime = Slime((level.))
    slime1 = Entity((random.randrange(400, 600), 1160), gameSprites, tileLayer)
    while running:
        screen.fill((8, 5, 28))
        # delta time
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # mouse config
        # pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - (screenWidth / 2) + player.rect.x, my - (screenHeight / 2) + player.rect.y
        # https://stackoverflow.com/questions/20162302/pygame-point-image-towards-mouse
        angle = 270 + math.atan2(mx - (screenWidth / 2), my - (screenHeight / 2)) * (180 / math.pi)

        # level updates
        if nextLevel:
            currentLevel += 1
            gameSprites.empty(), tileLayer.empty(), interactList.empty()
            player = Player((level.levels[currentLevel].get('playerPosX'), level.levels[currentLevel].get('playerPosY')), gameSprites)
            level = Level(gameSprites)
            level.loadMap()
            level.render()
            nextLevel = False

        if player.rect.colliderect(slime1.rect) or slime1.rect.right == player.rect.left or slime1.rect.left == player.rect.right:
            player.health -= slime1.damage

        if player.attacking and player.item.rect.colliderect(slime1.rect):
            slime1.health -= weaponData[player.belt[0]].get('damage')
        # print(angle)
        # print(player.health)
        # print(slime1.health)
        # function updates
        if slime1.health > 0:
            slime1.update(dt, player)
        elif slime1.health <= 0:
            slime1.kill()
        if player.health > 0:
            player.update(dt, dx, dy, angle)
        elif player.health <= 0:
            player.kill()

        print(player.rect)
        # print(nextLevel, currentLevel)
        cam_group.update()
        cam_group.render(player)
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
# _1_ 400 - 680 , 1160 _2_ 1175 - 1745, 380 | 1365 - 1950, 838 _3_ 1245 - 1540, 708 | 2020 - 2675, 968 | 2600 - 2950 ,1553 | 450 - 1785, 2150

game()
