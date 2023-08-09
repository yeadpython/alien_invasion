import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    bg_scrn = pygame.display.set_mode((ai_settings.bg_scrn_width, ai_settings.bg_scrn_height))
    pygame.display.set_caption("Do it yourself")
    
    ship = Ship(bg_scrn, ai_settings)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.screen_update(bg_scrn, ai_settings, ship)

run_game()














