#Sam Wonjae Lee

import sys    #Import modules
import pygame  

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))   #Set size of the screen
        pygame.display.set_caption("Alien Invasion Assignment 1")   #Set the pygame window name
        self.bg_color = (135, 206, 235)   #Set the colour of the background in rgb format

    def run_game(self):
        """Starts main loop for the game"""
        while True:     #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   #Ends pygame instance
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()   #Updates entire screen

game = AlienInvasion()
game.run_game()    #Runs game
