#Sam Wonjae Lee

import pygame, sys
from random import randint     #For randomization

class StarRandom:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/star.png')     #Brings image from file
        self.image = pygame.transform.scale(self.image, (30, 30))

    def blitme(self):
        for i in range(30):
            for j in range(30):
                randomnum = randint(-10, 10)     #Randomizing coordinate of star
                self.screen.blit(self.image, ((i*50 + randomnum), (j*50 + randomnum)))     #Seperates each star

class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))     #Set size of the screen
        pygame.display.set_caption('Alien Invasion Assignment 7')     #Set the pygame window name
        self.background_colour = (135, 206, 235)     #Set the colour of the background
        self.star = StarRandom(self)
        
    def run_game(self):
        """Starts main loop for the game"""
        self.screen.fill(self.background_colour)
        self.star.blitme()     #These lines are outside of while loop to prevent the stars to update each time
        
        while True:     #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
               
            pygame.display.flip()   #Updates entire screen 

        
game = AlienInvasion()
game.run_game()    #Runs game
