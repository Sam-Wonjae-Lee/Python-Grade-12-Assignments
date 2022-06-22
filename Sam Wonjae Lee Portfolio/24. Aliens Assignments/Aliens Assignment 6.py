#Sam Wonjae Lee

import pygame, sys

class StarGrid:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/star.png')     #Brings image from file
        self.image = pygame.transform.scale(self.image, (30, 30))

    def blitme(self):
        for i in range(5):     #Creates row of stars based on range
            for j in range(5):
                self.screen.blit(self.image, (i*100, j*100))    #Sets distance between stars

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))     #Set size of the screen
        pygame.display.set_caption('Alien Invasion Assignment 6')     #Set the pygame window name
        self.background_colour = (135, 206, 235)     #Set the colour of the background in rgb format
        self.star = StarGrid(self)
        
    def run_game(self):
        """Starts main loop for the game"""
        while True:     #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()     #Ends pygame instance
                    sys.exit()
            
            self.screen.fill(self.background_colour)
            self.star.blitme()
            pygame.display.flip()     #Updates entire screen

        
game = AlienInvasion()
game.run_game()    #Runs game
