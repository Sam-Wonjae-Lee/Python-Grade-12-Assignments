#Sam Wonjae Lee

import pygame, sys, time
from random import randint
from pygame.sprite import Sprite

class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.background_colour = (135, 206, 235)

        self.ship_speed = 1.5
        self.alien_speed = 1
        self.fleet_drop_speed = 1
        self.fleet_direction = 1
        self.bullet_speed = 1
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
        self.rect.midleft = self.screen_rect.midleft     #Start character at the middle left of the screen

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False     #Moving flags
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

class Alien(Sprite):
    def __init__(self, game):     #Inherit init 
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load('images/alien.png')     #Loads character image for 'images' folder
        self.image = pygame.transform.scale(self.image, (100, 100))     #Set character size
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        self.x = float(self.rect.x)     #x-coordinate of aliens
        
    def update(self):
        """Subtracts variable to make aliens move left"""
        self.x -= (self.settings.alien_speed)
        self.rect.x = self.x

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

class AliensInvasion:
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))      #Set size of the screen
        pygame.display.set_caption('Alien Invasion Assignment 10')     #Set the pygame window name

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()        
        self.fleet = pygame.sprite.Group()
        self.create_fleet()

    def run_game(self):
        """Starts main loop for the game"""
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_fleet()
            self.update_screen()

    def check_events(self):
        """Watch for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:     #Allows user to quit
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:     #When ship is moving
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_q:     #Quit
                    sys.exit()
                    pygame.exit()
                elif event.key == pygame.K_SPACE:     #For shooting bullets
                    self.fire_bullet()
                        
            elif event.type == pygame.KEYUP:     #When ship is not moving
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def fire_bullet(self):
        """Fires bullets wherever the ship is"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def update_fleet(self):
        self.fleet.update()

    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        for i in range(8):
            alien_number = randint(7, 10)
            row_number = randint(0, 10)
            self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width * alien_number * 1.5
        alien.y = alien_width * alien_number
        alien.rect.x = alien.x 
        alien.rect.y = alien_height * row_number
        self.fleet.add(alien)

    def update_bullets(self):
        """Updating and removing bullets when they are off screen"""
        length = len(self.fleet)
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                
        collisions = pygame.sprite.groupcollide(self.bullets, self.fleet, True, True)     #Check if a bullet hits an alien and removes it

        for alien in self.fleet.copy():
            if alien.rect.right <= 0:
                self.fleet.remove(alien)     #Removes alien
            if len(self.fleet) < length:
                alien_number = randint(7, 9)
                row_number = randint(0, 6)
                self.create_alien(alien_number, row_number)
                
    def update_screen(self):
        """Updates the entire screen with the current position of the ship and bullets"""
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.fleet.draw(self.screen)      
        pygame.display.flip()
    
game = AliensInvasion()
game.run_game()     #Runs game
