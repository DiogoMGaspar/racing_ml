import pygame
from typing import Callable

class Button:
    def __init__(self, coords: tuple[int, int], size: tuple[int, int], image: str, hovered_image: str, clicked_image: str, action: Callable = None):
        # Images
        self.current_image = image
        self.image = image
        self.hovered_image = hovered_image
        self.clicked_image = clicked_image

        # Functionality
        self.size = size
        self.rect = pygame.Rect(*coords, *size)
        self.action = action

        # Status
        self.hovered = False
        self.clicked = False
    
    def draw(self, display: pygame.Surface):
        "Must draw button every frame"
        current_image = pygame.image.load(self.current_image)
        resized_image = pygame.transform.scale(current_image, self.size)
        display.blit(resized_image, self.rect)

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            self.on_click(event)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
            self.on_release(event)

    def on_click(self, event: pygame.event.Event):
        if self.rect.collidepoint(event.pos) and not self.clicked:
            self.clicked = True
            
    def on_release(self, event: pygame.event.Event):
        self.clicked = False
        if self.rect.collidepoint(event.pos) and self.clicked:
            if self.action:
                self.action()

    def update(self, event: pygame.event.Event):
        """Must update the button for every event"""

        self.check_hover()
        self.handle_event(event)

        if self.clicked:
            self.current_image = self.clicked_image

        elif self.hovered:
            self.current_image = self.hovered_image

        else:
            self.current_image = self.image
