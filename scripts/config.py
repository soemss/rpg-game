import pygame

# Level Config #
tileLayer = pygame.sprite.Group()
interactList = pygame.sprite.Group()

bottom = pygame.transform.scale(pygame.image.load('assets/bottom.png'),
                                (65, 65))
bottomLeft = pygame.transform.scale(pygame.image.load('assets/bottomLeft.png'),
                                    (65, 65))
bottomRight = pygame.transform.scale(pygame.image.load('assets/bottomRight.png'), (65, 65))
left = pygame.transform.scale(pygame.image.load('assets/left.png'), (65, 65))
middle = pygame.transform.scale(pygame.image.load('assets/middle.png'), (65, 65))
right = pygame.transform.scale(pygame.image.load('assets/right.png'), (65, 65))
top = pygame.transform.scale(pygame.image.load('assets/top.png'), (65, 65))
topLeft = pygame.transform.scale(pygame.image.load('assets/topLeft.png'), (65, 65))
topRight = pygame.transform.scale(pygame.image.load('assets/topRight.png'), (65, 65))
flat = pygame.transform.scale(pygame.image.load('assets/flat.png'), (65, 65))
door = pygame.transform.scale(pygame.image.load('assets/door.png'), (65, 65))

# Item Config #
weaponData = {
    'fist': {'image': pygame.Surface((0, 0)), 'sizeX': 0, 'sizeY': 0},
    'stick': {'damage': .06, 'cooldown': 50, 'image': 'assets/items/weapons/stick.png', 'offset': 5, 'sizeX': 75,
              'sizeY': 20},
    'stone_sword': {'damage': 15, 'cooldown': 350, 'image': 'assets/items/weapons/stoneSword.png', 'offset': 0,
                    'sizeX': 90, 'sizeY': 27}
}

# Player Config
playerIdle = [pygame.transform.scale(pygame.image.load('assets/player/idle/playerIdle1.png'), (35, 72)),
              pygame.transform.scale(pygame.image.load('assets/player/idle/playerIdle2.png'), (35, 72)),
              pygame.transform.scale(pygame.image.load('assets/player/idle/playerIdle3.png'), (35, 72)),
              pygame.transform.scale(pygame.image.load('assets/player/idle/playerIdle4.png'), (35, 72))]
playerRun = [pygame.transform.scale(pygame.image.load('assets/player/run/playerRun1.png'), (35, 72)),
             pygame.transform.scale(pygame.image.load('assets/player/run/playerRun2.png'), (35, 72)),
             pygame.transform.scale(pygame.image.load('assets/player/run/playerRun3.png'), (35, 72)),
             pygame.transform.scale(pygame.image.load('assets/player/run/playerRun4.png'), (35, 72))]
playerCrouch = [pygame.transform.scale(pygame.image.load('assets/player/crouch/crouch1.png'), (35, 60)),
                pygame.transform.scale(pygame.image.load('assets/player/crouch/crouch2.png'), (35, 60)),
                pygame.transform.scale(pygame.image.load('assets/player/crouch/crouch3.png'), (35, 60)),
                pygame.transform.scale(pygame.image.load('assets/player/crouch/crouch4.png'), (35, 60))]

# Enemy Config
slimeMovement = [pygame.transform.scale(pygame.image.load('assets/enemy/slime/slime1.png'), (50, 50)),
                 pygame.transform.scale(pygame.image.load('assets/enemy/slime/slime2.png'), (50, 50))]
