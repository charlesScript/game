import pygame


# Definition de la class qui gere le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # Definition du constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 1.5
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 85
        self.origin_image = self.image
        self.angle = 0

    # Faire roter le projectile
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    # Supprimer tous les projectiles
    def remove(self):
        self.player.all_projectiles.remove(self)

    # Deplacer le projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # Condition si le projectile n'est plus sur l'ecran
        if self.rect.x > 1080:
            # Le supprimer
            self.remove()
