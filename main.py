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

    # Recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Appliquer l'ensemble des images du projectile
    game.player.all_projectiles.draw(screen)

    # Aplliquer l'ensemble des images du groupe de monstres
    game.all_monsters.draw(screen)

    # Appliquer le foward des monstres
    for monster in game.all_monsters:
        monster.forward()

    # Vefier la direction choisie du jour
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

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

            # Detecter si la touche CTRL est appuyée
            if event.key == pygame.K_SPACE:
                game.player.load_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
