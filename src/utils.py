import pygame
from math import sin

def offset_bounce(amplitude=2, interval=600):
    """Simple up and down animation"""
    offset = amplitude if (pygame.time.get_ticks() // interval) % 2 == 0 else - amplitude
    return offset