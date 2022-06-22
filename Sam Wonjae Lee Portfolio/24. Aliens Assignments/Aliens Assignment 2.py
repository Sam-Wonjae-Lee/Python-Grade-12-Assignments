#Sam Wonjae Lee

import sys    #Import modules
import pygame  

class Character:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        self.image = pygame.image.load('images/character.png')    #Loads character image for 'images' folder
        
        self.image = pygame.transform.scale(self.image, (100, 140))    #Set character size
        
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center     #Start character at the center of the screen

    def blitme(self):
        self.screen.blit(self.image, self.rect)    #Draw character at location

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))   #Set size of the screen
        pygame.display.set_caption("Alien Invasion Assignment 2")   #Set the pygame window name
        self.bg_color = (135, 206, 235)   #Set the colour of the background in rgb format
        self.character = Character(self)

    def run_game(self):
        """Starts main loop for the game"""
        while True:     #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   #Ends pygame instance
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()
            pygame.display.flip()   #Updates entire screen

game = AlienInvasion()
game.run_game()    #Runs game
