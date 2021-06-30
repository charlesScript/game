import pygame
from game import Game
from player import Player

pygame.init()

# ----- GENERER LA FENETRE DU JEU-----#
pygame.display.set_caption("Fire faling")
screen = pygame.display.set_mode((1080, 720))

# Importer l'arriere plan
background = pygame.image.load("assets/bg.jpg")

# Charger notre jeu
game = Game()

# Charger un joueur sur l'écran
player = Player()

running = True

"""Pour maintenir la fenetre ouverteCette boucle permettra d'ffectuer 
pleins de verifications par exemple si je le jeu est fini"""

while running:

    # Appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Vefier la direction choisie du jour
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    # Mettre à jour l'ecran
    pygame.display.flip()

    # Si le joueur ferme la fenetre
    for event in pygame.event.get():
        # Verifier fermeture de fenetre
        if event.type == pygame.QUIT:
            # Fermer la fénetre
            running = False
            pygame.quit()
            print("Jeu quiter")
        # Detecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False