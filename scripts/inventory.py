from scripts.config import *


def addGroup(self, group):
    group.add(self, layer=self.layer)


class Item(pygame.sprite.Sprite):
    layer = 3

    def __init__(self, group, player, item):
        super().__init__(group)
        # self.image = pygame.Surface((69, 69))
        self.image = pygame.transform.scale(
            pygame.image.load(weaponData[item].get('image')),
            (weaponData[item].get('sizeX'), weaponData[item].get('sizeY')))
        self.rect = self.image.get_rect()
        self.player = player

    def update(self, angle, selected):
        self.image = pygame.transform.scale(
            pygame.image.load(weaponData[selected].get('image')),
            (weaponData[selected].get('sizeX'),
             weaponData[selected].get('sizeY')))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=self.player.rect.center)


class Inventory:
    def __init__(self, player):
        super().__init__()
        self.player = player

    def update(self, angle, selected):
        if self.player.swapping:
            if self.player.primarySelected or self.player.secondarySelected:
                addGroup(self.player.item, self.player.group)
            if not self.player.primarySelected or self.player.secondarySelected:
                self.player.item.kill()

        # updates only when weapon is selected, to save resources
        if self.player.primarySelected or self.player.secondarySelected:
            self.player.item.update(angle, selected)
