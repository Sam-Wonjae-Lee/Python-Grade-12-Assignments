#Sam Wonjae Lee
import pygame, sys
from pygame.sprite import Sprite

class raindrop (Sprite) :
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load("images/raindrop.png")     #Loads raindrop for 'images' folder
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)     #y-coordinate for raindrop

    def update(self):
        self.rect.move_ip(0,1)     #Raindrops move vertically down by 1

        if self.rect.top > self.screen.get_rect().bottom:     #Checks to see if a raindrop goes offscreen then moves it to the top of the screen
            self.rect.move_ip(0,-self.screen.get_rect().bottom)
        else:     #Raindrop still moves down if its not offscreen
            self.rect.move_ip(0,1)

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Alien Invasion Assignment 9")
        self.bg_color = (0, 0, 0)
        self.raindrops = pygame.sprite.Group()
        self.create_rain()

    def run_game(self):
        while True:     #Watch for keyboard and mouse events
            self.raindrops.update()
            self.update_screen()
            self.update_rain()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)     #Draws raindrops
        pygame.display.flip()

    def print_drop(self, drop_number , row_number):
        """Creates and places a raindrop in its row"""
        drop = raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.rect.y = 2 *  drop.rect.height * row_number
        self.raindrops.add(drop)

    def create_rain(self):
        """Prints multiple rows of raindrops"""
        drop = raindrop(self)
        drop_width, drop_height = drop.rect.size

        horizontal = self.screen_width - drop_width
        rows = horizontal // drop_width

        vertical = self.screen_height
        coloumn = vertical // drop_height

        for row_number in range(coloumn):     #A row of raindrops is printed based on the coloumns
            for drop_number in range(rows):
                self.print_drop(row_number, drop_number)

    def update_rain(self):
        """Updates raindrops"""
        self.raindrops.update()

game = AlienInvasion()
game.run_game()     #Runs game
    
        
