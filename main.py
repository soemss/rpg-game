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
font = pygame.font.SysFont('Arial', 25)
fps = 60

enemyList = pygame.sprite.Group()
gameSprites = pygame.sprite.LayeredUpdates()
enemySpawns1 = [(random.randrange(400, 680), 1160), (random.randrange(1350, 1650), 1228)]
enemySpawns2 = [(random.randrange(480, 750), 123), (random.randrange(1175, 1745), 380),
                (random.randrange(1175, 1745), 380), (random.randrange(1365, 1950), 838),
                (random.randrange(350, 750), 1033)]
enemySpawns3 = [(random.randrange(1245, 1540), 708), (random.randrange(2020, 2675), 968),
                (random.randrange(2600, 2950), 1553), (random.randrange(2600, 2950), 1553),
                (random.randrange(2600, 2950), 1553), (random.randrange(450, 1785), 2150),
                (random.randrange(450, 1785), 2150), (random.randrange(450, 1785), 2150)]
currentLevel = -1
nextLevel = True


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.scroll = [0, 0]

    def render(self, player):
        # moves items based on player movement for 'scrolling camera' effect
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
    player = Player((level.levels[currentLevel].get('playerPosX'), level.levels[currentLevel].get('playerPosY')), gameSprites, 30)
    last_time = time.time()

    while running:
        screen.fill((8, 5, 28))
        # delta time
        dt = time.time() - last_time
        dt *= 60
        last_time = time.time()

        # mouse config
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - (screenWidth / 2) + player.rect.x, my - (screenHeight / 2) + player.rect.y
        # used this stackoverflow page for the item rotation angle
        # https://stackoverflow.com/questions/20162302/pygame-point-image-towards-mouse
        angle = 270 + math.atan2(mx - (screenWidth / 2), my -
                                 (screenHeight / 2)) * (180 / math.pi)

        # level updates
        if nextLevel:
            currentLevel += 1
            gameSprites.empty(), tileLayer.empty(), interactList.empty(), slimeGroup.empty()
            player = Player((level.levels[currentLevel].get('playerPosX'), level.levels[currentLevel].get('playerPosY')), gameSprites, player.health)
            level = Level(gameSprites)
            level.loadMap()
            level.render()

            # creates enemy objects whenever the level changes
            if currentLevel == 0:
                for slimes in range(len(enemySpawns1)):
                    if len(slimeGroup) <= len(enemySpawns1):
                        slimeEnemy = Entity(enemySpawns1[slimes], gameSprites, tileLayer, 0.01, 15)
                        slimeEnemy.add(slimeGroup)
            if currentLevel == 1:
                player.belt[0] = 'stone_sword'
                for slimes in range(len(enemySpawns2)):
                    if len(slimeGroup) <= len(enemySpawns2):
                        slimeEnemy = Entity(enemySpawns2[slimes], gameSprites, tileLayer, 0.03, 50)
                        slimeEnemy.add(slimeGroup)
            if currentLevel == 2:
                player.belt[0] = 'stone_sword'
                player.belt[1] = 'health_potion'
                for slimes in range(len(enemySpawns3)):
                    if len(slimeGroup) <= len(enemySpawns3):
                        slimeEnemy = Entity(enemySpawns3[slimes], gameSprites, tileLayer, 0.06, 80)
                        slimeEnemy.add(slimeGroup)
            nextLevel = False

        # function updates
        for slimeEnemy in slimeGroup:
            if slimeEnemy.health > 0:
                if player.rect.colliderect(
                        slimeEnemy.rect) or slimeEnemy.rect.right == player.rect.left or slimeEnemy.rect.left == player.rect.right:
                    player.health -= slimeEnemy.damage
                slimeEnemy.update(dt, player, slimeEnemy)
            elif slimeEnemy.health <= 0:
                slimeEnemy.kill()

        if player.health > 0:
            player.update(dt, dx, dy, angle)
        if player.health <= 0 or player.rect.y >= 3000:
            player.kill()
            screen.blit(font.render(f'You Died', False, (255, 255, 255)), (screenWidth / 2 - 50, screenHeight / 2))
        if currentLevel == 2 and len(slimeGroup.sprites()) == 0:
            screen.blit(font.render(f'You Win', False, (255, 255, 255)), (screenWidth / 2, screenHeight / 2))
        cam_group.update()
        cam_group.render(player)
        screen.blit(font.render(f'{round(player.health)}', False, (255, 255, 255)), (50, 500))
        screen.blit(font.render(f'Enemies Left: {len(slimeGroup.sprites())}', False, (255, 255, 255)), (50, 525))
        pygame.display.flip()
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

game()
