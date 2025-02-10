import pygame
from math import sqrt
from constants import WHITE, RED

class Point:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.label = None

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)
        if self.label:
            font = pygame.font.Font(None, 36)
            label = font.render(self.label, True, WHITE)
            screen.blit(label, (self.x + 5, self.y + 5))
    
    def get_distance(self, other_point):
        return sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)