import pygame



class Ship(object):
    def __init__(self, screen, ai_setting):
        self.screen = screen
        self.image = pygame.image.load('./images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ai_setting = ai_setting

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def updat(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_setting.ship_speed_factor
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx