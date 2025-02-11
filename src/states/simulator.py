import pygame
from core.state_manager import StateManager

class Simulator:
    def __init__(self, display: pygame.Surface, state_manager: StateManager):
        self.display = display
        self.state_manager = state_manager

    def run(self):
        pass