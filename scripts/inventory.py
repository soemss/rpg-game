from scripts.config import *


def addGroup(self, group):
    group.add(self, layer=self.layer)


class Item(pygame.sprite.Sprite):
    layer = 3

    def __init__(self, group, player, item):
        super().__init__(group)
        self.image = pygame.transform.scale(
            pygame.image.load(weaponData[item].get('image')), (weaponData[item].get('sizeX'), weaponData[item].get('sizeY')))
        self.rect = self.image.get_rect()
        self.player = player

    def update(self, angle, selected):
        if self.player.selected is not None:
            self.image = pygame.transform.scale(pygame.image.load(weaponData[selected].get('image')), (weaponData[selected].get('sizeX'), weaponData[selected].get('sizeY')))
            self.image = pygame.transform.rotate(self.image, angle)
            self.rect = self.image.get_rect(center=self.player.rect.center)


class Inventory:
    def __init__(self, player):
        super().__init__()
        self.player = player

    def update(self, angle, selected):
        if self.player.swapping:
            if self.player.selected is not None:
                addGroup(self.player.item, self.player.group)
            if self.player.selected is None:
                self.player.item.kill()
        if self.player.selected is not None:
            self.player.item.update(angle, selected)
