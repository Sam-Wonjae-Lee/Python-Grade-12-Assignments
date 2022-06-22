import sys    #Import modules
import pygame  

class Character:
    """Manages Ship"""
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('images/rocket.png')    #Loads character image for 'images' folder
        
        self.image = pygame.transform.scale(self.image, (100, 140))    #Set character size
        
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center     #Start character at the center of the screen

        self.moving_right = False     #Moving flags
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)    #Used to create canvas

    def update(self):
        """Updates and prevents the ship's position based on the movement"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
            
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

        if self.moving_right and self.rect.right >= self.screen_rect.right:
            self.moving_right = False
            self.rect.x -= 1
            
        if self.moving_left and self.rect.left <= self.screen_rect.left:
            self.moving_left = False
            self.rect.x += 1

        if self.moving_up and self.rect.top <= self.screen_rect.top:
            self.moving_up = False
            self.rect.y += 1

        if self.moving_down and self.rect.bottom >= self.screen_rect.bottom:
            self.moving_down = False
            self.rect.y -= 1

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))   #Set size of the screen
        pygame.display.set_caption("Alien Invasion Assignment 3")   #Set the pygame window name
        self.bg_color = (135, 206, 235)   #Set the colour of the background in rgb format

        self.character = Character(self)

    def run_game(self):
        """Starts main loop for the game"""
        while True:     #Watch for keyboard and mouse events
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:     #Allows user to quit
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:     #When ship is moving
                    if event.key == pygame.K_RIGHT:
                        self.character.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.character.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.character.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.character.moving_down = True
                        
                elif event.type == pygame.KEYUP:     #When ship is not moving
                    if event.key == pygame.K_RIGHT:
                        self.character.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.character.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.character.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.character.moving_down = False

            
            self.screen.fill(self.bg_color)
            self.character.update()
            self.character.blitme()
            pygame.display.flip()     #Updates entire screen            

game = AlienInvasion()
game.run_game()    #Runs game
