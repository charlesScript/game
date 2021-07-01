import pygame


# Class qui gere la notion de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 545
        self.velocity = 1

    def forward(self):
        self.rect.x -= self.velocity
