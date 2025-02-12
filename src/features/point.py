import pygame
from math import sqrt
from typing import Optional
from constants import OFF_WHITE, RED

class Point:
    def __init__(self, coords: tuple[float, float], radius: int = 10):
        self.x: float = coords[0]
        self.y: float = coords[1]
        self.radius: int = radius
        self.label: Optional[str] = None

    def draw(self, display: pygame.Surface):
        pygame.draw.circle(display, RED, (int(self.x), int(self.y)), self.radius)

        # Debugging: Display point's label
        if self.label:
            font = pygame.font.Font(None, 36)
            label = font.render(self.label, True, OFF_WHITE)
            display.blit(label, (self.x + 5, self.y + 5))
    
    def get_distance(self, other_point: "Point"):
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)