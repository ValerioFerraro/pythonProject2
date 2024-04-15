import sys
import pygame

class AlienInvasion:
    """overall class to manage assets and behavior"""
    def __init__(self):
        """initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Tastatur und Mausereignisse.
            for event in pygame.event.get():
                if event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

            #zuletzt gezeichneter bildschirm wird sichtbar gemacht
            pygame.display.flip()

#erstellt eine Spielinstanz und führt das Spiel aus.
if __name__== '__main__':
    ai = AlienInvasion()
    ai.run_game()




