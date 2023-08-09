import pygame

class Ship():
    def __init__(self, bg_scrn, ai_settings) -> None:
        
        self.bg_scrn = bg_scrn
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.image_rect = self.image.get_rect()
        self.bg_scrn_rect = bg_scrn.get_rect()

        self.image_rect.centerx = self.bg_scrn_rect.centerx
        self.image_rect.bottom = self.bg_scrn_rect.bottom

        self.center = float(self.image_rect.centerx)

        self.move_right = False
        self.move_left = False

    def update(self):
        if self.move_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.image_rect.centerx = self.center

    def blitme(self):
        self.bg_scrn.blit(self.image, self.image_rect)









