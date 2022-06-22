#Sam Wonjae Lee

import pygame, sys
from pygame.sprite import Sprite

class Settings:

    def __init__(self):
        self.background_colour = (135, 206, 235)     #Set the colour of the background in rgb format 

        #For bullet
        self.bullet_speed = 0.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = (255, 0, 0)

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.png')     #Loads character image for 'images' folder
        self.image = pygame.transform.scale(self.image, (100, 100))     #Set character size
        self.image = pygame.transform.rotate(self.image, 270)     #Rotate character
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft    #Start character at the middle left of the screen

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False     #Moving flags
        self.moving_left = False
        self.moving_up = False     
        self.moving_down = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)     #Used to create canvas

    def update(self):
        """Updates or prevents the ship's position based on the movement"""
        if self.moving_up:
            self.rect.y -= 1.0
        if self.moving_down:
            self.rect.y += 1.0

        if self.moving_up and self.rect.top <= self.screen_rect.top:
            self.moving_up = False
            self.rect.y += 1.0

        if self.moving_down and self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
            self.rect.y -= 1.0

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()     #Inherit init 
        self.screen = game.screen
        self.settings = game.settings
        self.colour = self.settings.bullet_colour

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)     #Create bullet next to ship
        self.rect.midright = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Make bullet constantly move right"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen, self.colour, self.rect)


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((500, 500))     #Set size of the screen
        pygame.display.set_caption('Alien Invasion Assignment 5')     #Set the pygame window name

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Starts main loop for the game"""
        while True: 
            self.check_events()
            self.ship.update()

            for bullet in self.bullets.copy():
                if bullet.rect.right >= 500:     #Removes bullet when it is off-screen - 500 is based on screen size
                    self.bullets.remove(bullet)

            self.bullets.update()
            self.update_screen()


    def check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #Allows user to quit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:     #When ship is moving
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                        
            elif event.type == pygame.KEYUP:     #When ship is not moving
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                    
                elif event.key == pygame.K_SPACE:     #For shooting bullets
                    self.fire_bullet()

    def fire_bullet(self):
        """Fires bullets wherever the ship is"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_screen(self):
        """Updates the entire screen with the current position of the ship and bullets"""
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  
        pygame.display.flip()     #Updates entire screen


        
game = AlienInvasion()
game.run_game()     #Runs game

