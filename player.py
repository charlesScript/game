import pygame
from projectile import Projectile


# Creer une classe qui représente le joueur
# Super class python qui permet d'initialiser des objet de class
# jeu dans python
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 1
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    # Charger le projectile
    def load_projectile(self):
        self.all_projectiles.add(Projectile(self))

    # methode permettant de deplacer le joueur en utilisant sa vitesse exprimee en pixels
    def move_right(self):
        self.rect.x += self.velocity

    # methode permettant de deplacer le joueur en utilisant sa vitesse exprimee en pixels
    def move_left(self):
        self.rect.x -= self.velocity
