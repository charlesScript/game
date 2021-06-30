import pygame
from player import Player


# Classe representant le jeu
class Game:

    def __init__(self):
        # Generer le joueur
        self.player = Player()
        self.pressed = {}

