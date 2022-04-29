from scripts.config import *
clock = pygame.time.Clock()


class Entity(pygame.sprite.Sprite):
    layer = 2

    def __init__(self, pos, group, tileList):
        super().__init__(group)
        # animations
        self.frame = 0
        self.animation = slimeMovement[0]
        # properties
        self.image = pygame.transform.scale(slimeMovement[self.frame], (50, 50))
        self.originalImage = self.image
        self.rect = self.image.get_rect(center=pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.airTimer = 0
        self.speed = 1
        self.gravity = 0
        self.health = 15
        self.damage = .02
        self.tileList = tileList

    def movement(self, dt, player):
        self.velocity = pygame.Vector2(0, 0)
        if player.rect.right < self.rect.left:
            self.velocity[0] -= self.speed
        elif player.rect.left > self.rect.right:
            self.velocity[0] = self.speed

        self.gravity += 0.8 * dt
        self.velocity[1] += self.gravity
        if self.velocity[1] > 20:
            self.velocity[1] = 20

    def collision(self, dt):
        # horizontal collision
        self.rect.x += self.velocity[0] * dt
        tileList = self.tileList
        for tile in tileList:
            if self.rect.colliderect(tile.rect):
                if self.velocity[0] < 0:
                    self.rect.left = tile.rect.right
                elif self.velocity[0] > 0:
                    self.rect.right = tile.rect.left
        # vertical collision
        self.rect.y += self.velocity[1] * dt
        for tile in tileList:
            if self.rect.colliderect(tile.rect):
                if self.velocity[1] > 0:
                    self.rect.bottom = tile.rect.top
                    self.airTimer = 0
                    self.gravity = 0
                elif self.velocity[1] < 0:
                    self.rect.top = tile.rect.bottom
                    self.gravity = 0

    def animate(self):
        self.animation = slimeMovement
        self.frame += 0.06
        if self.frame >= len(self.animation):
            self.frame = 0
        self.image = self.animation[int(self.frame)]
        self.originalImage = self.image

    def update(self, dt, player):
        self.airTimer += 1
        self.animate(), self.movement(dt, player), self.collision(dt)
