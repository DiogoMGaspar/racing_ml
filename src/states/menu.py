import pygame
import utils
from core.state_manager import StateManager
from ui.button import Button

class Menu:
    def __init__(self, display: pygame.Surface, state_manager: StateManager):
        self.display = display
        self.state_manager = state_manager

        # Background
        self.background = pygame.image.load("assets/art/red_bg.png")
        self.car = pygame.image.load("assets/art/car_bg.png")

        # Buttons
        start_button_str = "assets/buttons/silver_button_start"
        self.start_button = Button((300, 300), (192, 64), f"{start_button_str}.png", f"{start_button_str}_hovered.png", f"{start_button_str}_clicked.png", self.start_game)

        settings_button_str = "assets/buttons/silver_button_settings"
        self.settings_button = Button((500, 500), (192, 64), f"{settings_button_str}.png", f"{settings_button_str}_hovered.png", f"{settings_button_str}_clicked.png", self.open_settings)

    def start_game(self):
        self.state_manager.set_state("Simulator")

    def open_settings(self):
        pass
    
    def handle_event(self, event):
        # Buttons
        self.start_button.update(event)
        self.settings_button.update(event)

    def run(self):
        offset = utils.offset_bounce()

        # Background
        self.display.blit(self.background, (0,0))
        self.display.blit(self.car, (0, -3 + offset))

        # Buttons
        self.start_button.draw(self.display)
        self.settings_button.draw(self.display)
        
