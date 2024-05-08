import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """General class to manage resources and gameplay."""
    def __init__(self):
        """Game initialization and creating resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
    
    def run_game(self):
        """Creating main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()